# Generated by Django 4.2.3 on 2023-08-16 10:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="content",
            old_name="git_repository",
            new_name="web_address",
        ),
        migrations.AlterUniqueTogether(
            name="content",
            unique_together={("web_address", "filename")},
        ),
    ]
