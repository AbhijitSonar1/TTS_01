# Generated by Django 3.2.9 on 2022-01-29 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0048_alter_tracker_sysdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='ScreenShot',
            field=models.ImageField(default='', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='Sysdate',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 20, 9, 43, 803718), null=True),
        ),
    ]
