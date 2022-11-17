from datetime import datetime,date
from email import message
from django.shortcuts import render,HttpResponse,redirect
from .models import AddTaskData, AddProjectdata,AddEmpData,Tracker,loginapi,SuperUsers
import json
from datetime import timedelta
import datetime
from loguru import logger
from django.contrib import messages 
 

def Dashboard(request):
    if "email" in request.session and "id" in request.session:
        all_Empdata=AddEmpData.objects.all()
        all_data=loginapi.objects.filter(toady_date__contains=date.today())
        # print(all_data)
        userloginlist = []
        # print(all_data,"---------------------------")
        for ii in all_data:
            # print(ii.pk)
            userloginlist.append(int(ii.uid))
        trackdatalst = []
        # (------------Screenshot---------------")
        for i in all_Empdata:
            userid = str(i.pk)
            data = Tracker.objects.filter(datetime__contains=date.today(),Userid=userid).order_by('-pk')
            if len(data) > 0:
                trackdatalst.append(data[0])
                # print(len(data))
        
        # (------------Count all data---------------")
        countproject=AddProjectdata.objects.all
        print(countproject)      
        logger.success(" Dashboard Opened Successfully ")
        
    else:
        logger.debug(" Dashboard Dashboard has Poblem ")
        return redirect("app_pr:login")
    return render(request,"Dashboard.html",{"empdata":all_Empdata,"all_data":all_data,"trackerapi":trackdatalst,"userloginlist":userloginlist})



def screenshot(request,Userid):
    if "email" in request.session and "id" in request.session:
        # all_empdata=AddEmpData.objects.all()
        last_two_daydtatas =datetime.datetime.now().date() - timedelta(2)
        current_datetime = datetime.datetime.now().date().today()
        tdata=Tracker.objects.filter(datetime__lte=current_datetime,datetime__gte=last_two_daydtatas,Userid=Userid).order_by('-pk')
        context = {'tdata':tdata} 
# print(last_two_day)
        logger.info(" Screenshot Added Successfully ")
        Tracker.objects.filter(datetime__lte=datetime.datetime.now()-timedelta(days=10)).delete()
        return render(request,"All_screenshot.html",context)
            
            #......................DATA ENTRY SECTION...................#

def converDate(val):
    d =datetime.datetime.strptime(val, "%d-%m-%Y")
    return d.strftime("%Y-%m-%d")
def convertprdate(val):
    d=datetime.datetime.strptime(val,"%d-%m-%Y")
    return d.strftime("%Y-%m-%d")

def convert_tracker_date(data): 
    val=str(data)
    val1=val.split(" ")
    month_name=val1[1]
    year_name=val1[4]
    date_name=val1[2]
    datetime_object =datetime.datetime.strptime(month_name, "%b")
    month_number = datetime_object.month
    # print(month_number)
    # print(month)
    tr_date=str(year_name) + "-" + str(month_number) + "-"  + str( date_name)
    # print(tr_date)
    return tr_date
    
# convert_tracker_date("Wed Dec 2 19:41:18 2022")

            #......................Adding Project DATA ......................#
def ProjectDetail(request):
    all_empdata=AddEmpData.objects.all()
    all_prdata=AddProjectdata.objects.all()
    if "email" in request.session and "id" in request.session:
        if request.method=="POST":
            prid=request.POST.get("prid")
            prname=request.POST.get("prname")
            prduration=request.POST.get("prduration")
            prstartdate=request.POST.get("prstartdate")
            prhandalar=request.POST.get("prhandalar")
            prdatails=request.POST.get("txtprdtail")
            prstatus=request.POST.get("prstatus")
            prstartdate = converDate(prstartdate)
            add_prdata=AddProjectdata(prid=prid,prname=prname,prduration=prduration,prstartdate=prstartdate,prhandalar=prhandalar,prdatails=prdatails,prstatus=prstatus)
            add_prdata.save()
            logger.success("Project added succefully ")
            return redirect("app_pr:ProjectDetail")
        return render(request,"ProjectDetail.html",{"data":all_empdata,"prdata":all_prdata})
    else:
            return redirect("app_pr:login")



                   #.......................Adding Task data................#   
def TaskDetail(request):
    if "email" in request.session and "id" in request.session:
        all_prdata=AddProjectdata.objects.all()
        all_data = AddEmpData.objects.all()
        all_taskdata=AddTaskData.objects.all()
        if request.method=="POST":
            Task_ID=request.POST.get("taskid")
            Project_ID=request.POST.get("Taskprid")
            Task_Name=request.POST.get("taskname")
            User=request.POST.get("User")
            Task_duration=request.POST.get("taskduration")
            Current_Time=request.POST.get("Currenttime")    
            Task_Status=request.POST.get("taskstatus")
            Task_Details=request.POST.get("taskdetail")
            print(Task_ID,Project_ID,Task_Name,User,Task_duration,Current_Time,Task_Status,Task_Details)
            add_Task=AddTaskData(Task_ID=Task_ID,Project_ID=Project_ID,Task_Name=Task_Name,User=User,Task_duration=Task_duration,Current_Time=Current_Time,Task_Status=Task_Status,Task_Details=Task_Details)
            add_Task.save() 
            logger.success("Task added succefully ")
            return redirect("app_pr:Taskdetail")   
        return render(request,"TaskDetails.html", {"prdata":all_prdata,"empdata":all_data,"taskdata":all_taskdata})



                #....................Admin Login/Logout..........................#
def login(request):
    all_data=SuperUsers.objects.all()
    if request.method=="POST":
        email=request.POST.get("txtemail")
        password=request.POST.get("txtpassword")
        print(email,password)
        for i in all_data:
            # print(i.useremail,i.password)
            if i.useremail==email and i.password==password:
                print("login")
                request.session['email']=email
                request.session['id']=i.pk
                request.session['type']=i.type
                request.session['userfname']=i.userfname
                request.session['userlname']=i.userlname 
                # print(request.session['type'])
                logger.success("Login Successfully")
                return redirect("app_pr:Dashboard")
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect("app_pr:login")  
    return render(request,"login.html")


def adminlogout(request):   
    del  request.session['email']
    del  request.session['id']
    return redirect("app_pr:login")
 

                   #.......................Adding Employee Data................#   
def add_employee(request):
    check_SuperUsers=SuperUsers.objects.get(pk=request.session['id'])
    all_data = AddEmpData.objects.all()
    if "email" in request.session and "id" in request.session:
        if check_SuperUsers.type == "Admin" or check_SuperUsers.type =="Superadmin":
            if request.method=="POST" and request.FILES.get('image'):  
                fname=request.POST.get("txtFirstName")
                lname=request.POST.get("txtLasttName")
                email=request.POST.get("txtemail")
                joindate=request.POST.get("joindate")
                password=request.POST.get("txtpassword")
                designation=request.POST.get("designation")
                department=request.POST.get("txtdepartment")
                Gender=request.POST.get("Gender")
                mobile=request.POST.get("mobile")
                dob=request.POST.get("dateOfBirth")
                dob = converDate(dob)
                joindate = converDate(joindate)
                print(dob,joindate)
                Address=request.POST.get("txtarea")
                uploadimage= request.FILES.get("image")
                add_data=AddEmpData(fname=fname,lname=lname,email=email,password=password,designation=designation,joindate=joindate,department=department,Gender=Gender,mobile=mobile,dob=dob,Address=Address,uploadimage=uploadimage)
                add_data.save()
                logger.success(" Employee Added Successfully ")
                return redirect("app_pr:add_employee")
            return render(request,"add_employee.html", {"data":all_data})
        else:
            logger.error(" you Dont have access to go On this Page  ")
            return redirect("app_pr:Dashboard")
    else:
        logger.error(" you Dont have access to go On that Page  ")
        return redirect("app_pr:login")
            


def EmpDetail(request):
    all_empdata=AddEmpData.objects.all()
    return render(request,"empdeatail.html",{"empdata":all_empdata})
                 
def user_profile(request,id):
    all_empdata=AddEmpData.objects.get(pk=id)
    all_empdataa=AddEmpData.objects.all()
    all_prdata=AddProjectdata.objects.filter(prhandalar=str(id))
        # for j in all_prdata:
        #     # print(i.pk)
        #     prname=(j.prname)
    return render(request,"user_profile.html",{'all_empdata':all_empdata,'prnames':all_prdata,'all_empdataa':all_empdataa})

def Superusers(request):
    all_Superuser_data=SuperUsers.objects.all()
    check_SuperUsers=SuperUsers.objects.get(pk=request.session['id'])
    if "email" in request.session and "id" in request.session:
        if check_SuperUsers.type =="Superadmin":
            if request.method=="POST":  
                if request.method=="POST":
                    usertype=request.POST.get("type")
                    userfname=request.POST.get("fname")
                    userlname=request.POST.get("lname")
                    useremail=request.POST.get("email")
                    password=request.POST.get("password")

                    # print(usertype,userfname,userlname,useremail,password)
                    add_superuser=SuperUsers(type=usertype,userfname=userfname,userlname=userlname,useremail=useremail,password=password)
                    add_superuser.save()
                    logger.success(" Superusers Added Successfully ")
                    return redirect("app_pr:SuperUsers")
            return render (request,'superuser_form.html',{'all_Superuser_data':all_Superuser_data})
        else:
            logger.error(" you Dont have access to go On this Page  ")
            return redirect("app_pr:Dashboard")
    else:
        logger.error(" you Dont have access to go On that Page  ")
        return redirect("app_pr:login")

def lock_screen(request):
    superadmin_Data=SuperUsers.objects.all()
    if request.method == "POST":
        password=request.POST.get("pass")
        for i in superadmin_Data:
            if i.password == password:
                return redirect("app_pr:Dashboard")
            else:
                return redirect("app_pr:lock_screen")
    return render(request,'lock_screen.html',{'superadmin_Data':superadmin_Data})   
    #..................................... API SECTION.............................................#    

                    #..................Employee Login/Logout Api...................#
@logger.catch
def loginuser(request):
    all_data=AddEmpData.objects.all()   
    loginstatus_datas = loginapi.objects.filter(toady_date=date.today()) 
    loginstatus_datas_list = []
    for ldata in loginstatus_datas:
        loginstatus_datas_list.append(int(ldata.uid))
    # print(loginstatus_datas_list)
    if request.method =="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        current_datetime = datetime.datetime.now()
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        # today_date = date.today()
        # print(email,password)
        plist = []
        tdict={}
        for i in all_data:
            # print(i.email)
            if i.email==email and i.password==password:
                pdata = AddProjectdata.objects.filter(prhandalar=i.pk)
                for pi in pdata:
                    plist.append(pi.prname)
                    tdict[pi.prname] =[]
                    tdata = AddTaskData.objects.filter(User=i.pk,Project_ID=pi.pk)
                    for ti in tdata:
                        # ti.Task_Name         
                        tdict[pi.prname].append(ti.Task_Name)
                d1={
                    "userid":i.pk,
                    "firstname":i.fname,
                    "Lastname":i.lname,
                    "email":i.email,
                    "password":i.password,
                    "designation":i.designation,
                    "department":i.department,
                    "Gender":i.Gender,
                    "mobile":i.mobile,
                    "Address":i.Address }
                mainDict={
                    "udeatils":d1,
                    "Project":plist,
                    "task":tdict,
                }

                #to maintain status 
                #first check login status data is exist or not
                if int(i.pk) in loginstatus_datas_list:
                    print("yes data exists")
                    updatestatusdata = loginapi.objects.filter(toady_date=date.today(),uid=i.pk)[0]         #it showing data as indexwise 0 means first data
                    updatestatusdata.status = "Login"
                    updatestatusdata.datetime=current_datetime
                    updatestatusdata.starttime=current_time
                    updatestatusdata.endtime=current_time
                    updatestatusdata.toady_date=date.today()
                    updatestatusdata.save()
                    logger.success(" login successfully")

                else:
                    logger.INFO(" NEW  user Logined ")
                    # print("noooo")
                    add_status=loginapi(uid=i.pk,status="Login",datetime=current_datetime,starttime=current_time,endtime=current_time,toady_date=date.today())
                    add_status.save()
                # print(mainDict)                    
                return HttpResponse(json.dumps({"status":200,"response":mainDict},),content_type="application/json")  
        else:
            logger.error(" Data Not Found ")
            return HttpResponse(json.dumps({"status":400,"response":"Data Not Found"}),content_type="application/json")
    else:
        logger.error(" Method Is not Allow ")
        data = json.dumps({"status":400,"response":"Method Is not Allow"})
        return HttpResponse(data,content_type="application/json")
  
def logout(request): 
    loginstatus_datas = loginapi.objects.filter(toady_date=date.today()) 
    loginstatus_datas_list = []
    for ldata in loginstatus_datas:
        loginstatus_datas_list.append(int(ldata.uid))
    if request.method=="POST":
        current_datetime = datetime.datetime.now()
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        userid=request.POST.get("userid")
        print("same")
        if int(userid) in loginstatus_datas_list:
            print("yes data exists")
            updatestatusdata = loginapi.objects.filter(toady_date=date.today(),uid=int(userid))[0]         #it showing data as indexwise 0 means first data
            updatestatusdata.status = "Logout"
            updatestatusdata.datetime=current_datetime
            updatestatusdata.starttime=current_time
            updatestatusdata.endtime=current_time
            updatestatusdata.toady_date=date.today()
            updatestatusdata.save()
            messages.success(request, "logout Successfully")
            logger.success("logout Successfully ")
            return HttpResponse(json.dumps({"status":200,"response":"data added successfully"}),content_type="application/json")
        else:
            logger.error("data not found ")
            return HttpResponse(json.dumps({"status":400,"response":"data not found"}),content_type="application/json") 
    else:
        logger.error("method not found")
        return HttpResponse(json.dumps({"status":401,"response":"method not found"}),content_type="application/json")                


                        #......................Tracker Api.......................#
@logger.catch
def trackerdata(request):
    all_data=AddEmpData.objects.all() 
    if request.method=="POST" :
        userid = request.POST.get("userid")
        pid = request.POST.get("pid")
        tid =request.POST.get("tid")
        screenshot = request.FILES.get("screenshot")
        datetime= request.POST.get("datetime")
        currenttime=request.POST.get("curretntime")
        todaystime=request.POST.get("todaystime")
        totaltime=request.POST.get("totaltime")
        mousecelickevent=request.POST.get("mouseclicks")
        keyboardclickevent=request.POST.get("keybordclicks")
        datetime=convert_tracker_date(datetime)
        
        project=AddProjectdata.objects.filter(prhandalar=userid,prname=pid).order_by('-pk')    
        for i in project:
           
            prid=i.pk
            # print(prid)
                
            task=AddTaskData.objects.filter(User=userid,Project_ID=i.pk)
            for j in task:
                if j.Task_Name == tid:
                    li=[]
                    trid=j.pk
                    print(trid)

                    # if len(str(trid)) > 0:
                    #     li.append(str(trid))
                    # print(len(li))
        addtraker=Tracker(Userid=userid,projctid=prid,taskid=trid,ScreenShot=screenshot,datetime=datetime,cuurenttime=currenttime,todaystime=todaystime,totaltime=totaltime,mouseClickevent=mousecelickevent,keyboardClickevent=keyboardclickevent)
        addtraker.save()        
        logger.success("tracker started ")
        return HttpResponse(json.dumps({"status":200,"response":"data added successfully"}),content_type="aplication/json")
    else:      
        logger.error("tracker not started ")
        return HttpResponse(json.dumps({"status":200,"response":"data added successfully"}),content_type="aplication/json")


#........................................EDIT SECTION.........................................#

            #............................Employee EDIT ..............................#
def Empedit(request,id):
    all_data=AddEmpData.objects.get(pk=id)
    if id==0:
        pass
    else:
        all_data=AddEmpData.objects.get(pk=id)
        if "update" in request.POST:
            fname=request.POST.get("txtFirstName")
            lname=request.POST.get("txtLasttName")
            email=request.POST.get("txtemail")
            # joindate=request.POST.get("joindate")
            password=request.POST.get("txtpassword")
            designation=request.POST.get("designation")
            department=request.POST.get("txtdepartment")
            Gender=request.POST.get("Gender")
            mobile=request.POST.get("mobile")
            dob=request.POST.get("dateOfBirth")
            Address=request.POST.get("txtarea")                
            uploadimage= request.FILES.get("image")
            oldimage=request.POST.get("oldimage")
            dob = converDate(dob)
            # print(uploadimage)
            # print(oldimage)
            all_data.fname=fname
            all_data.lname=lname
            all_data.email=email
            # all_data.joindate=joindate
            all_data.password=password
            all_data.designation=designation
            all_data.department=department
            all_data.Gender=Gender
            all_data.mobile=mobile
            all_data.dob=dob
            all_data.Address=Address         
            # all_data.oldimage=oldimage
            if uploadimage == None:
                # all_data.uploadimage=uploadimage
                pass
            else:
                all_data.uploadimage=uploadimage
                    
            all_data.save()
            return redirect("app_pr:EmpDetail")
        if "Edit" in request.POST:
            print("Update")
            return render(request,"Editdata/edit_empdata.html",{"empdata":all_data})
        elif "delete" in request.POST:
            all_data.delete()
            # print("delete")
            return redirect("app_pr:EmpDetail")
        logger.success(" Employee Edit Successfully ")

    return render(request,"Editdata/edit_empdata.html")



        #............................Project EDIT ..............................#
# "data":all_empdata
def Projectedit(request,id):
    all_prdata=AddProjectdata.objects.get(pk=id)
    all_empdata=AddEmpData.objects.all()
    if id==0:
        pass
    else:
        if "update" in request.POST:
            prid=request.POST.get("prid")
            prname=request.POST.get("prname")
            prduration=request.POST.get("prduration")
            prstartdata=request.POST.get("prstartdate")
            prhandalar=request.POST.get("prhandalar")
            prdatails=request.POST.get("txtprdtail")
            prstatus=request.POST.get("prstatus")
            prstartdate = converDate(prstartdata)
            
            all_prdata.prid=prid
            all_prdata.prname=prname
            all_prdata.prduration=prduration
            all_prdata.prstartdate=prstartdate
            all_prdata.prhandalar=prhandalar
            all_prdata.prdatails=prdatails
            all_prdata.prstatus=prstatus
            # print(all_prdata.prstartdata)
            all_prdata.save()
            return redirect("app_pr:ProjectDetail")
        if "Edit" in request.POST:
            logger.success("Update")
            return render(request,"Editdata/edit_projectdata.html",{"prdata":all_prdata,"data":all_empdata})
        elif "delete" in request.POST:
            all_prdata.delete()
            # print("delete")
            return redirect("app_pr:ProjectDetail")
        logger.success(" Employee Edit Successfully ")    
    return render(request,"Editdata/edit_projectdata.html")


            #............................Task EDIT ..............................#
def Taskedit(request,id):
    all_tdata=AddTaskData.objects.get(pk=id)
    all_taskdata=AddTaskData.objects.all()
    all_prdata=AddProjectdata.objects.all()
    all_empdata=AddEmpData.objects.all()
    if id==0:
        pass
    else:
        if "update" in request.POST:
            Task_ID=request.POST.get("taskid")
            Project_ID=request.POST.get("Taskprid")
            Task_Name=request.POST.get("taskname")
            User=request.POST.get("User")
            Task_duration=request.POST.get("taskduration")
            Current_Time=request.POST.get("Currenttime")    
            Task_Status=request.POST.get("taskstatus")
            Task_Details=request.POST.get("taskdetail")
            all_tdata.Task_ID=Task_ID
            all_tdata.Project_ID=Project_ID
            all_tdata.Task_Name=Task_Name
            all_tdata.User=User
            all_tdata.Task_duration=Task_duration
            all_tdata.Current_Time=Current_Time
            all_tdata.Task_Status=Task_Status
            all_tdata.Task_Details=Task_Details
            all_tdata.save()
            return redirect("app_pr:Taskdetail")

        if "Edit" in request.POST:
            print("Update")
            return render(request,"Editdata/edit_taskdata.html",{"taskdata":all_tdata,"empdata":all_empdata,"prdata":all_prdata,})
        elif "delete" in request.POST:
            all_tdata.delete()
            # print("delete")
            return redirect("app_pr:Taskdetail")
    return render(request,"Editdata/edit_taskdata.html",{"tdata":all_taskdata,"empdata":all_empdata})


            #............................SuperUsers EDIT ..............................#
def edit_superuser_form(request,id):
    all_Superuser_data=SuperUsers.objects.get(pk=id)
    if id ==0:
        pass
    else:
        if "update" in request.POST:
            usertype=request.POST.get("type")
            userfname=request.POST.get("fname")
            userlname=request.POST.get("lname")
            useremail=request.POST.get("email")
            password=request.POST.get("password")
                
            all_Superuser_data.type=usertype
            all_Superuser_data.userfname=userfname
            all_Superuser_data.userlname=userlname
            all_Superuser_data.useremail=useremail
            all_Superuser_data.password=password
            print(usertype)
            all_Superuser_data.save()
            return redirect("app_pr:SuperUsers")
        elif "Edit" in request.POST:
            return render(request,'Editdata/edit_superuser_form.html',{'Superuser_data':all_Superuser_data})

        elif "delete" in request.POST:
            all_Superuser_data.delete()
            return redirect('app_pr:SuperUsers')
    return render(request,'Editdata/edit_superuser_form.html')