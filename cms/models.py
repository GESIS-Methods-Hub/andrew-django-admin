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
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    subtitle = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Subtitle"
    )
    abstract = models.TextField(null=True, blank=True, verbose_name="Abstract")
    cover_image = models.FileField(
        upload_to="cover_image/", null=True, blank=True, verbose_name="Cover image"
    )

    def __str__(self):
        if self.parent_collection is None:
            return self.title

        return f"{self.parent_collection.__str__()}/{self.title}"

    def get_absolute_url(self):
        return reverse("show_collection", kwargs={"pk": self.pk})


class Content(models.Model):
    web_address = models.CharField(max_length=200, verbose_name="Web address")
    filename = models.CharField(max_length=50, verbose_name="File name")
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
        return f"{self.web_address} + {self.filename}"

    def get_absolute_url(self):
        return reverse("show_content", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (
            "web_address",
            "filename",
        )
