FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV NEXT_PUBLIC_WEBSITE_URL=http://localhost:3000
ENV NEXT_PUBLIC_META_TITLE=XDB
ENV NEXT_PUBLIC_META_DESCRIPTION=LoremENV 
ENV NEXT_PUBLIC_META_IMAGE=https://cheeff.uz/images/logo.png
ENV NEXT_PUBLIC_META_KEYWORDS=XDB
ENV NEXT_PUBLIC_API_URL=http://localhost:8000
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
