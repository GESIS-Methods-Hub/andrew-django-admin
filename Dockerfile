FROM  ubuntu:22.04 AS dev

COPY requirements.txt requirements.txt

RUN DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt-get update \
    && apt-get install -y tzdata python3 python3-dev python3-pip libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

WORKDIR /var/andrew-django-admin

COPY docker-entrypoint.sh /var/andrew-django-admin/docker-entrypoint.sh

ENTRYPOINT ["/var/andrew-django-admin/docker-entrypoint.sh"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

FROM dev AS prod

RUN python3 -m pip install gunicorn

ADD . /var/andrew-django-admin

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8080", "andrew.wsgi"]
