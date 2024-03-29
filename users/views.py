from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'post':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             username= form.cleaned_data.get('username')
             messages.success(request, f' Account Created for {username}!')
             return redirect('info-home')
    else:
        form = UserCreationForm()
    return render (request, 'users/register.html',{'form': form})
