# Generated by Django 3.2.9 on 2022-01-18 04:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0023_addprojectdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddEmpData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=35)),
                ('designation', models.CharField(max_length=35)),
                ('department', models.CharField(max_length=35)),
                ('Gender', models.CharField(max_length=35)),
                ('mobile', models.CharField(max_length=35)),
                ('dob', models.DateField()),
                ('Address', models.CharField(max_length=35)),
            ],
        ),
        migrations.AlterField(
            model_name='addtaskdata',
            name='Current_Time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
