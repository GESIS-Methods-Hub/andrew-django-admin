# Generated by Django 4.2.3 on 2023-08-11 14:42

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Affiliation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "department",
                    models.CharField(max_length=200, verbose_name="Department"),
                ),
                ("city", models.CharField(max_length=200, verbose_name="City")),
                (
                    "country",
                    django_countries.fields.CountryField(
                        max_length=2, verbose_name="Country"
                    ),
                ),
                ("url", models.URLField(verbose_name="Website")),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "orcid",
                    models.CharField(max_length=19, unique=True, verbose_name="Name"),
                ),
                ("url", models.URLField(verbose_name="Website")),
                (
                    "affiliation",
                    models.ManyToManyField(
                        to="cms.affiliation", verbose_name="Affiliation"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="content",
            name="author",
            field=models.ManyToManyField(to="cms.affiliation", verbose_name="Author"),
        ),
    ]
