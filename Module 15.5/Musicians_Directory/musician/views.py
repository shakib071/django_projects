from django.shortcuts import render,redirect
from . import forms
# Create your views here.

def create(request):
    if request.method== 'POST':
        mus_form = forms.MusicianForm(request.POST)
        if mus_form.is_valid():
            mus_form.save()
            return redirect('create_musician')
    else:
        mus_form=forms.MusicianForm()

    return render(request,'create_musician.html',{'form' : mus_form})

        
