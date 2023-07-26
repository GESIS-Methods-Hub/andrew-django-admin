# Generated by Django 4.2.3 on 2023-07-26 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0004_content_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="abstract",
            field=models.TextField(verbose_name="Abstract"),
        ),
        migrations.AlterField(
            model_name="collection",
            name="parent_collection",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cms.collection",
                verbose_name="Parent collection",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="title",
            field=models.CharField(
                max_length=200, primary_key=True, serialize=False, verbose_name="Title"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="collection",
            field=models.ManyToManyField(
                to="cms.collection", verbose_name="Collection"
            ),
        ),
        migrations.AlterField(
            model_name="content",
            name="file",
            field=models.CharField(max_length=50, verbose_name="File name"),
        ),
        migrations.AlterField(
            model_name="content",
            name="git_repository",
            field=models.CharField(max_length=200, verbose_name="Git repository"),
        ),
        migrations.AlterField(
            model_name="content",
            name="group",
            field=models.CharField(
                choices=[("P", "Package"), ("T", "Tutorial")],
                default="T",
                max_length=1,
                verbose_name="Type",
            ),
        ),
    ]
