from django.db import models


class Collection(models.Model):
    parent_collection = models.ForeignKey("self", null=True,  blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, primary_key=True)
    abstract = models.TextField()


class Content(models.Model):
    git_repository = models.CharField(max_length=200)
    file = models.CharField(max_length=50)
    collection = models.ManyToManyField(Collection)

    class Meta:
        unique_together = (
            "git_repository",
            "file",
        )
