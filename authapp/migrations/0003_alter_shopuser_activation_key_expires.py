# Generated by Django 3.2.3 on 2021-07-04 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210703_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 6, 13, 12, 40, 537797, tzinfo=utc)),
        ),
    ]