from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def filters(request):
    data={'txt' : ['python','is','fun'],'date' : datetime.datetime.now(),
          'age' : 22 , "txt1": 'christmas','txt2' : 'shakib',
           'txt3' : "python is fun" , 'txt4' : [{'name': 'Josh', 'age': 19},{'name': 'Dave', 'age': 22},{'name': 'Joe', 'age': 31},],
            'txt5' : 'I am a Student'}
    
    return render(request,'filters.html', data)

