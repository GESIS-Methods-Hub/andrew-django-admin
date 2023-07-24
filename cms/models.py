from django.db import models


class Collection(models.Model):
    parent_collection = models.ForeignKey("self", null=True,  blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, primary_key=True)
    abstract = models.TextField()

    def __str__(self):
        return self.title

class Content(models.Model):
    git_repository = models.CharField(max_length=200)
    file = models.CharField(max_length=50)
    collection = models.ManyToManyField(Collection)

    def __str__(self):
        return f"{self.git_repository} + {self.file}"

    class Meta:
        unique_together = (
            "git_repository",
            "file",
        )
