# Generated by Django 3.2.3 on 2021-05-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0004_alter_social_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
