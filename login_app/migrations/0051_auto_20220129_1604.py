# Generated by Django 3.2.9 on 2022-01-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0050_auto_20220129_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='cuurenttime',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='todaystime',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='totaltime',
            field=models.TimeField(default=''),
        ),
    ]