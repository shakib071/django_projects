
from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    # return HttpResponse("This is home page")
    return render(request,'base.html')

def home(request):
    # return HttpResponse("This is home page")
    return render(request,'home.html')


