# Generated by Django 3.2.9 on 2022-01-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0053_loginapi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginapi',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='loginapi',
            name='enddate',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='loginapi',
            name='starttime',
            field=models.TimeField(),
        ),
    ]