from django.contrib import admin
from . import models
 
# Register your models here.
 
class ManagerAdmin(admin.ModelAdmin):
  list_display = ("dishTitle",  "created")
 
admin.site.register(models.MenuItem, ManagerAdmin)
