# Generated by Django 3.2.9 on 2022-01-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_alter_addprojectdata_prid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTaskData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_ID', models.CharField(max_length=35)),
                ('Project_ID', models.CharField(max_length=25)),
                ('Task_Name', models.CharField(max_length=35)),
                ('Task_duration', models.CharField(max_length=35)),
                ('Current_Time', models.CharField(max_length=35)),
                ('Task_Status', models.CharField(max_length=35)),
                ('Task_Details', models.CharField(max_length=35)),
            ],
        ),
    ]