from django.shortcuts import render
from .forms import ModelForm

# Create your views here.


def model(request):
    form = ModelForm()

    return render(request,"model.html",{'form': form})

