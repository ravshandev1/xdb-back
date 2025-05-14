from celery import Celery, shared_task
from dotenv import dotenv_values
from requests import post, patch, get

ENV = dotenv_values(".env")
app = Celery(__name__)
app.conf.broker_url = f"redis://redis:6379/0"
app.conf.result_backend = f"redis://redis:6379/0"
app.conf.broker_connection_retry_on_startup = True
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Tashkent')
app.autodiscover_tasks()

@shared_task
def get_data_from_tax_task(ids: list[dict]):
    token = post(f"{ENV.get('TAX_API')}/water-supply/api/authenticate/login", json={"username": "WaterSupply", "password": "Pa$$w0rd"})
    for j in ids:
        res = get(f"{ENV.get('TAX_API')}/water-supply/api/water-supply/get-gravel-info",
                  headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token.text}'},
                  params={"tin": j['tin'], "periodYear": j['year'], "periodMonth": j['month']})
        if res.status_code >= 500:
            diff_count = "Soliqni API si ishlamadi!"
        elif res.status_code >= 400:
            diff_count = res.json()["text"]
        else:
            diff_count = res.json()['data']['count'] if res.json()['data'] else "Malumot olishda xatolik"
        res = patch(f"{ENV.get('BASE_URL')}/application/{j['id']}", json={"diff_count": str(diff_count)})
    return "Got the response"
