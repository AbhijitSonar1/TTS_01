# Generated by Django 3.2.9 on 2022-01-12 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0010_addtaskdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtaskdata',
            old_name='prid',
            new_name='Prid',
        ),
    ]
