from django.contrib import admin
from .models import AddTaskData, AddProjectdata,AddEmpData,Tracker,loginapi,SuperUsers

# # Register your models here.
admin.site.register(AddEmpData)
admin.site.register(AddProjectdata)
admin.site.register(AddTaskData)
admin.site.register(Tracker)
admin.site.register(loginapi)
admin.site.register(SuperUsers)