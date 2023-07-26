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

### How to run the app in the developmen environment?

```{bash}
python manage.py migrate && python manage.py runserver
```

### How to create create a new migration after change the database model?

```{bash}
python manage.py makemigrations
```
