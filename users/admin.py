from django.contrib import admin

from . import models
class UsersAdmin(admin.ModelAdmin):
    pass 

admin.site.register(models.UsersProfile,UsersAdmin)
