from django.shortcuts import render
from .forms import Forms

# Create your views here.


def form(request):
    form = Forms()

    return render(request,"form.html",{'form': form})


