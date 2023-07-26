from django.db import models
from django.urls import reverse


class Collection(models.Model):
    parent_collection = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Parent collection",
    )
    title = models.CharField(max_length=200, primary_key=True, verbose_name="Title")
    abstract = models.TextField(verbose_name="Abstract")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show_collection", kwargs={"collection_id": self.pk})


class Content(models.Model):
    git_repository = models.CharField(max_length=200, verbose_name="Git repository")
    file = models.CharField(max_length=50, verbose_name="File name")
    collection = models.ManyToManyField(Collection, verbose_name="Collection")

    PACKAGE_GROUP = "P"
    TUTORIAL_GROUP = "T"
    GROUP_CHOICES = [
        (PACKAGE_GROUP, "Package"),
        (TUTORIAL_GROUP, "Tutorial"),
    ]
    group = models.CharField(
        max_length=1, choices=GROUP_CHOICES, default=TUTORIAL_GROUP, verbose_name="Type"
    )

    enable = models.BooleanField(default=True, verbose_name="Enable")

    def __str__(self):
        return f"{self.git_repository} + {self.file}"

    def get_absolute_url(self):
        return reverse("show_content", kwargs={"content_id": self.pk})

    class Meta:
        unique_together = (
            "git_repository",
            "file",
        )
