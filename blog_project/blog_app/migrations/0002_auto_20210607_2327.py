# Generated by Django 3.1.4 on 2021-06-07 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 7, 17, 57, 25, 126946, tzinfo=utc)),
        ),
    ]
