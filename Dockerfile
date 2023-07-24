FROM  ubuntu:22.04 AS dev

RUN DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt-get update \
    && apt-get install -y tzdata python3 python3-pip

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt && rm -f requirements.txt

WORKDIR /var/andrew-django-admin

FROM dev AS prod

RUN apt install python3-dev libpq-dev nginx -y

ADD . /var/andrew-django-admin

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangokubernetesproject.wsgi"]
