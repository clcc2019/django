from django.shortcuts import render
from django.http import HttpResponse

from .models import HostName

def index(request):
    list = HostName.objects.all()
    context = {'list':list}
    return render(request,'index.html',context)

def search_form(request):
    pass
def insert(request):
    pass    
    
