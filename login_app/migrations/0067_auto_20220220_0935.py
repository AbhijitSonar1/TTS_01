# Generated by Django 3.2.9 on 2022-02-20 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0066_addempdata_joindate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddEmpData',
        ),
        migrations.DeleteModel(
            name='AddProjectdata',
        ),
        migrations.DeleteModel(
            name='AddTaskData',
        ),
        migrations.DeleteModel(
            name='loginapi',
        ),
        migrations.DeleteModel(
            name='SuperUsers',
        ),
        migrations.DeleteModel(
            name='Tracker',
        ),
    ]