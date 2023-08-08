# Contributing

In the `CONTRIBUTING.md`, we use [`micromamba`](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) but you can use [`mamba`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html) or [`conda`](https://docs.conda.io/).

## How-to

### How to get the source code?

```{bash}
git clone git@github.com:GESIS-Methods-Hub/andrew-django-admin.git
```

### How to load the development environment?

```{bash}
docker compose up
```

### How to load the demo database?

With the development environment running, in another terminal, execute

```{bash}
docker compose exec django python3 manage.py loaddata demo/db.json
```

### How to create create a new migration after change the database model?

```{bash}
docker compose exec django python3 manage.py makemigrations
```

### How to update the demo database?

```{bash}
docker compose exec django python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```

### How to render the Helm chart?

```{bash}
helm template render helm/andrew-django-admin/
```

### How to preview Helm chart in Minikube?

```{bash}
sudo mkdir -p /mnt/andrew-django-admin/postgres
```

```{bash}
minikube start
```

```{bash}
kubectl \
    create \
    secret \
    generic \
    andrew-django-admin \
    --from-literal=django_secret_key='django-insecure-7mpt%30s!5bye-ve4n4m6v7e6$1t24%v8)(##w5phnn75hiy06'
```

```{bash}
kubectl \
    create \
    secret \
    generic \
    andrew-django-admin-postgres \
    --from-literal=password='123456' \
    --from-literal=user='andrew' \
    --from-literal=db='andrew'
```

```{bash}
helm upgrade \
    andrew-django-admin \
    ./helm/andrew-django-admin \
    --install \
    --create-namespace \
    --history-max 1
```

### How to get a shell from Kubernetes pod?

```{bash}
kubectl \
    exec \
    --stdin \
    --tty \
    pod_name \
    -- /bin/bash
```
