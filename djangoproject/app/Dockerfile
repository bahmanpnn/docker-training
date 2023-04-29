FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV DJANGO_SUPERUSER_PASSWORD admin123

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install django gunicorn

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email admin@gmail.com --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi
 