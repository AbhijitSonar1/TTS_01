# Generated by Django 3.2.9 on 2022-01-30 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0051_auto_20220129_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='trid',
        ),
    ]