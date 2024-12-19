2from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class RegisterSchema(BaseModel):
    name: Optional[str] = None
    phone: str
    password: str
    confirm_password: str


class LoginSchema(BaseModel):
    phone: str
    password: str


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str


class UserSchema(BaseModel):
    id: int
    name: Optional[str] = None
    phone: str
    superuser: bool
    created_at: datetime

    @classmethod
    def to_dict(cls, item):
        return {
            "id": item.id,
            "name": item.name,
            "phone": item.phone,
            "superuser": item.superuser,
            "created_at": item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None


class ApplicationSchema(BaseModel):
    id: int
    code: int
    date: date
    area: str
    river: str
    plot: str
    address: str
    stir: int
    dsi: str
    subject_name: str
    count: int
    diff_count: str
    different: str
    status: str
    created_at: datetime

    @classmethod
    def to_dict(cls, item):
        different = item.diff_count
        if isinstance(item.diff_count. str):
            try:
                different = item.count - int(item.diff_count)
            except ValueError:
                try:
                    different = float(item.count) - float(item.diff_count)
                except ValueError:
                    pass
        return {
            "id": item.id,
            "code": item.code,
            "date": item.date.strftime("%Y-%m-%d"),
            "area": item.area,
            "river": item.river,
            "plot": item.plot,
            "address": item.address,
            "stir": item.stir,
            "dsi": item.dsi,
            "subject_name": item.subject_name,
            "count": item.count,
            "diff_count": item.diff_count,
            "different": different,
            "status": item.status,
            "created_at": item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class ApplicationUpdateSchema(BaseModel):
    status: str
    diff_count: str


class ApplicationPeriodQuery(BaseModel):
    limit: int = 50
    offset: int = 1
    year: Optional[int] = None
    month: Optional[int] = None
    stir: Optional[int] = None
