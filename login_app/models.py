from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from datetime import datetime,date 
# # Employee Data
class AddEmpData(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=35)
    email=models.CharField(max_length=35)
    password=models.CharField(max_length=35)
    designation=models.CharField(max_length=35)
    joindate=models.DateField()
    department=models.CharField(max_length=35)
    Gender=models.CharField(max_length=35)
    mobile=models.IntegerField()
    dob=models.DateField()
    Address=models.CharField(max_length=200)
    uploadimage=models.ImageField(upload_to="profile_image/",default="")


#Project Data
class AddProjectdata(models.Model):
    prid=models.CharField(max_length=35)    
    prname=models.CharField(max_length=25)
    prduration=models.CharField(max_length=25)
    # prduration=models.TimeField(auto_now=True)
    prstartdate=models.DateField( auto_now_add=False,auto_now=False,blank=True,null=True)
    prhandalar=models.CharField(max_length=35)
    prdatails=models.CharField(max_length=250)
    prstatus=models.CharField(max_length=35) 

# Task Data
class AddTaskData(models.Model):
    Task_ID=models.CharField(max_length=20)
    Project_ID=models.CharField(max_length=25)
    Task_Name=models.CharField(max_length=35)
    User=models.CharField(max_length=20)
    Task_duration=models.CharField(max_length=35)
    Current_Time= models.TimeField()
    Task_Status=models.CharField(max_length=35)
    Task_Details=models.CharField(max_length=250) 

class Tracker(models.Model):
     Userid=models.CharField(max_length=35)
     projctid=models.CharField(max_length=35)
     taskid=models.CharField(max_length=35)
     ScreenShot=models.ImageField(upload_to="Screenshot/",default="")
     datetime=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
     cuurenttime=models.TimeField(default="")
     todaystime=models.TimeField(default="")
     totaltime=models.TimeField(default="")
     mouseClickevent=models.CharField(max_length=35)
     keyboardClickevent=models.CharField(max_length=35)

     
class loginapi(models.Model):
    uid=models.CharField(max_length=35)
    status=models.CharField(max_length=35)
    datetime=models.DateTimeField()
    starttime=models.TimeField()
    endtime=models.TimeField()
    toady_date=models.DateField()


class SuperUsers(models.Model):
    type=models.CharField(max_length=35)
    userfname=models.CharField(max_length=30)
    userlname=models.CharField(max_length=30)
    useremail=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

   
    #TIME_ZONE = 'Asia/Kolkata' 
    
    # height_field=None, width_field=None, 
