# Generated by Django 4.2.3 on 2023-08-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_rename_git_repository_content_web_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='web_address',
            field=models.CharField(max_length=200, verbose_name='Web address'),
        ),
    ]
