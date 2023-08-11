from django.db import models
from django.urls import reverse

from django_countries.fields import CountryField


class Affiliation(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    department = models.CharField(max_length=200, verbose_name="Department")
    city = models.CharField(max_length=200, verbose_name="City")
    country = CountryField(verbose_name="Country")
    url = models.URLField(max_length=200, verbose_name="Website")

    def __str__(self):
        return f"{self.department}, {self.name}"


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    orcid = models.CharField(max_length=19, unique=True, verbose_name="ORCID ID")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Website")
    affiliation = models.ManyToManyField(Affiliation, verbose_name="Affiliation")

    def __str__(self):
        return f"{self.name} ({self.orcid})"


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
    git_repository = models.CharField(max_length=200, verbose_name="Git repository")
    filename = models.CharField(max_length=50, verbose_name="File name")
    author = models.ManyToManyField(Author, verbose_name="Author")
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
        return f"{self.git_repository} + {self.filename}"

    def get_absolute_url(self):
        return reverse("show_content", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (
            "git_repository",
            "filename",
        )
