from django.contrib import admin
from .models import HostName



class HostNameAdmin(admin.ModelAdmin):


    list_display = ('ID','name','ctime','ssl_otime','ssl')
    list_filter = ['name']




admin.site.register(HostName,HostNameAdmin)
