# Admin interface for `andrew` powered by Django

Docker Image: https://hub.docker.com/r/gesiscss/andrew-django-admin

Helm Chart Repository: https://gesis-methods-hub.github.io/andrew-django-admin (see [`index.yml`](https://gesis-methods-hub.github.io/andrew-django-admin/index.yml))

[`andrew` (Aggregator for Navigatable Discoverable Reproducible and Educational work)](https://github.com/GESIS-Methods-Hub/andrew) is a R package to help with the creation of a website that shows a collection of tutorials or vignette. This [Django](https://www.djangoproject.com/) web app provides a user interface to manager the collection of tutorials or vignette and a REST API (powered by [Django REST framework](https://www.django-rest-framework.org/)) to be consumed by `andrew`.

## Features

- [X] Admin panel (`/admin`)
- [X] Web form to add content (`/cms`)
- [X] API endpoint to get **enabled** content (`/api/content`)
- [X] API endpoint to get navigation tree of **enabled** content (`/api/collection`)

## Development

For development, we recomommend to use [Docker Compose](https://docs.docker.com/compose/).

On your terminal, execute

```{bash}
docker compose up
```

and your development environment should be ready. This repository is bind mounted into the container, database migrations are executed, and the Django server is started. Read the log in the terminal for more details.

The credentials for the admin interface is

```
User: admin
Password: 123456
```

A collection of how-to is included in [CONTRIBUTING.md](CONTRIBUTING.md).

## Production

For production, we recommned to run the provided Helm Chart on Kubernetes.
