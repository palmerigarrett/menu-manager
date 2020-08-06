from django.contrib import admin
from . import models
 
# Register your models here.
 
class ManagerAdmin(admin.ModelAdmin):
  list_display = ("dishTitle",  "created")

class CourseAdmin(admin.ModelAdmin): 
  list_display = ("name",)

admin.site.register(models.MenuItem, ManagerAdmin)
admin.site.register(models.Course, CourseAdmin)
