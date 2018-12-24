from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    file = request.FILES.get('file')
        
    return render(request,'upfile.html')
