# Generated by Django 3.2.9 on 2022-01-29 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0041_remove_tracker_screenshot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='SystemDate',
            new_name='Sysdate',
        ),
    ]