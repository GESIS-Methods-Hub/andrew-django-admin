FROM  ubuntu:22.04 AS dev

RUN DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt-get update \
    && apt-get install -y tzdata python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt && rm -f requirements.txt

WORKDIR /var/andrew-django-admin

FROM dev AS prod

RUN apt-get update && \
    apt install python3-dev libpq-dev nginx -y && \
    python3 -m pip install gunicorn && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD . /var/andrew-django-admin

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8080", "andrew.wsgi"]
