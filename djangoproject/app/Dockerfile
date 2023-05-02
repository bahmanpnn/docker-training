FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV DJANGO_SUPERUSER_PASSWORD admin123

RUN mkdir /app
WORKDIR /app

RUN apk update
RUN apk add --no-cache gcc python3-dev musl-dev mariadb-dev

RUN pip install --upgrade pip
RUN pip install django gunicorn mysqlclient

RUN apk install del gcc python3-dev musl-dev 

CMD whlie ! python3 manage.py sqlflush > /dev/null 2>&1 ;do sleep 1; done && \
    python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email admin@gmail.com --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi

#this command make terminal to dont show errors
# CMD python3 manage.py makemigrations --noinput && \
#     while ! python3 manage.py migrate --noinput > /dev/null 2>&1 ;do sleep 1; done && \
#     python3 manage.py collectstatic --noinput && \
#     python3 manage.py createsuperuser --user admin --email admin@gmail.com --noinput; \
#     gunicorn -b 0.0.0.0:8000 config.wsgi

# CMD python3 manage.py makemigrations --noinput && \
#     while ! python3 manage.py migrate --noinput ;do sleep 1; done && \
#     python3 manage.py collectstatic --noinput && \
#     python3 manage.py createsuperuser --user admin --email admin@gmail.com --noinput; \
#     gunicorn -b 0.0.0.0:8000 config.wsgi

# CMD sleep 10 &&
#     python3 manage.py makemigrations --noinput && \
#     python3 manage.py migrate --noinput && \
#     python3 manage.py collectstatic --noinput && \
#     python3 manage.py createsuperuser --user admin --email admin@gmail.com --noinput; \
#     gunicorn -b 0.0.0.0:8000 config.wsgi
 