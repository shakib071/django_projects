from django.shortcuts import render,redirect

from . import forms
from . import models
# Create your views here.


def create(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('create_album')
        
    else:
        album_form = forms.AlbumForm()
    return render(request,'create_album.html',{'form':album_form})

def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    
    album_form =  forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form =  forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request, 'create_album.html',{'form' : album_form})


def delete_album(request,id):
    post = models.Album.objects.get(pk=id)

    post.delete()

    return redirect('homepage')


