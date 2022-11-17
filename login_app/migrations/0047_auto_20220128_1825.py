# Generated by Django 3.2.9 on 2022-01-29 02:25

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0046_auto_20220128_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='trid',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tracker',
            name='Sysdate',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 18, 25, 15, 372344)),
        ),
    ]
