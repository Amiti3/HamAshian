# Generated by Django 3.0.8 on 2020-07-18 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adOfRoommate', '0002_auto_20200717_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adofroommate',
            name='date_publish',
            field=models.DateField(default=datetime.datetime(2020, 7, 19, 2, 13, 40, 505720)),
        ),
    ]
