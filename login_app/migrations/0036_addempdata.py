# Generated by Django 3.2.9 on 2022-01-22 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0035_delete_addempdata'),
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
    ]
