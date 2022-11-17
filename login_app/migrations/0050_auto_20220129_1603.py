# Generated by Django 3.2.9 on 2022-01-30 00:03

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0049_auto_20220128_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='USername',
            new_name='Userid',
        ),
        migrations.RenameField(
            model_name='tracker',
            old_name='trdate',
            new_name='datetime',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='Sysdate',
        ),
        migrations.AddField(
            model_name='tracker',
            name='cuurenttime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracker',
            name='todaystime',
            field=models.TimeField(default=datetime.datetime(2022, 1, 30, 0, 0, 44, 605620, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracker',
            name='totaltime',
            field=models.TimeField(default=datetime.datetime(2022, 1, 30, 0, 3, 16, 620898, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
