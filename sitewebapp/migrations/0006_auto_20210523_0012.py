# Generated by Django 3.2.3 on 2021-05-23 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitewebapp', '0005_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choose',
            name='icon',
        ),
        migrations.AddField(
            model_name='choose',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]