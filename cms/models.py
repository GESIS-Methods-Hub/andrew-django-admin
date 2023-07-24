from django.db import models

class Content(models.Model):
    git_repository = models.CharField(max_length=200)
    file = models.CharField(max_length=50)
