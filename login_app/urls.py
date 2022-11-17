from django.contrib import admin
from django.urls import path
from login_app import views
app_name="app_pr"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProjectDetail/',views.ProjectDetail,name="ProjectDetail"),
    path('EmpDetail/',views.EmpDetail,name="EmpDetail"),
    path('add_employee/',views.add_employee,name="add_employee"),
    path("Taskdetail/",views.TaskDetail,name="Taskdetail"),
    path('Dashboard/',views.Dashboard,name="Dashboard"),
    path('user_profile/<int:id>',views.user_profile,name="user_profile"),

    path('screenshot/<int:Userid>',views.screenshot,name="screenshot"),
    path('',views.login,name="login"),
    path('adminlogout',views.adminlogout,name="adminlogout"),
    path('SuperUsers/',views.Superusers,name="SuperUsers"),
    path('lock_screen/',views.lock_screen,name="lock_screen"),    


    #api 
    path("loginuser/",views.loginuser,name="loginuser"),
    path("trackerdata/",views.trackerdata,name="trakerdata"),
    path("logout/",views.logout,name="logout"),
    #Edit
    path('EditEmployeeData/<int:id>',views.Empedit,name="Empedit"),
    path('EditTaskData/<int:id>',views.Taskedit,name="Taskedit"),
    path('EditProjectData/<int:id>',views.Projectedit,name="PRedit"),
    path('edit_superuser_form/<int:id>',views.edit_superuser_form,name="edit_superuser_form"),





    


]
