# Generated by Django 3.2.9 on 2022-01-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0021_alter_addtaskdata_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtaskdata',
            name='Current_Time',
            field=models.TimeField(),
        ),
    ]