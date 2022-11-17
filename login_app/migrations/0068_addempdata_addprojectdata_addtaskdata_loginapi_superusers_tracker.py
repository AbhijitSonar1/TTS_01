# Generated by Django 3.2.9 on 2022-02-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0067_auto_20220220_0935'),
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
                ('joindate', models.DateField()),
                ('department', models.CharField(max_length=35)),
                ('Gender', models.CharField(max_length=35)),
                ('mobile', models.CharField(max_length=35)),
                ('dob', models.DateField()),
                ('Address', models.CharField(max_length=35)),
                ('uploadimage', models.ImageField(default='', upload_to='profile_image/')),
            ],
        ),
        migrations.CreateModel(
            name='AddProjectdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prid', models.CharField(max_length=35)),
                ('prname', models.CharField(max_length=25)),
                ('prduration', models.CharField(max_length=25)),
                ('prstartdate', models.DateField(blank=True, null=True)),
                ('prhandalar', models.CharField(max_length=35)),
                ('prdatails', models.CharField(max_length=35)),
                ('prstatus', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='AddTaskData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_ID', models.CharField(max_length=20)),
                ('Project_ID', models.CharField(max_length=25)),
                ('Task_Name', models.CharField(max_length=35)),
                ('User', models.CharField(max_length=20)),
                ('Task_duration', models.CharField(max_length=35)),
                ('Current_Time', models.TimeField()),
                ('Task_Status', models.CharField(max_length=35)),
                ('Task_Details', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='loginapi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=35)),
                ('status', models.CharField(max_length=35)),
                ('datetime', models.DateTimeField()),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('toady_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SuperUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=35)),
                ('userfname', models.CharField(max_length=30)),
                ('userlname', models.CharField(max_length=30)),
                ('useremail', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Userid', models.CharField(max_length=35)),
                ('projctid', models.CharField(max_length=35)),
                ('taskid', models.CharField(max_length=35)),
                ('ScreenShot', models.ImageField(default='', upload_to='Screenshot/')),
                ('datetime', models.DateField(blank=True, null=True)),
                ('cuurenttime', models.TimeField(default='')),
                ('todaystime', models.TimeField(default='')),
                ('totaltime', models.TimeField(default='')),
                ('mouseClickevent', models.CharField(max_length=35)),
                ('keyboardClickevent', models.CharField(max_length=35)),
            ],
        ),
    ]