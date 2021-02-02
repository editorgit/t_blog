FROM python:3.8.1-buster as blogapp

RUN mkdir -p /var/www/var/media
RUN mkdir -p /var/www/var/static
WORKDIR /var/www/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /var/www/app
