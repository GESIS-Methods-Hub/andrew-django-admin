# Generated by Django 4.2.3 on 2023-07-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0005_alter_collection_abstract_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="enable",
            field=models.BooleanField(default=True, verbose_name="Enable"),
        ),
    ]
