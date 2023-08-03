# Contributing

In the `CONTRIBUTING.md`, we use [`micromamba`](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) but you can use [`mamba`](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html) or [`conda`](https://docs.conda.io/).

## How-to

### How to get the source code?

```{bash}
git clone git@github.com:GESIS-Methods-Hub/andrew-django-admin.git
```

### How to create the development environment?

```{bash}
micromamba create -n andrew-django-admin -f env.yaml
```

### How to load the development environment?

```{bash}
micromamba activate andrew-django-admin
```

### How to load the demo database?

```{bash}
python manage.py loaddata demo/db.json
```

### How to run the app in the developmen environment?

```{bash}
python manage.py migrate && python manage.py runserver
```

### How to create create a new migration after change the database model?

```{bash}
python manage.py makemigrations
```

### How to update the demo database?

```{bash}
python manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```

### How to render the Helm chart?

```{bash}
helm template render helm/andrew-django-admin/
```

### How to preview Helm chart in Minikube?

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
