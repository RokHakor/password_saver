from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required(login_url="login")
def index(request):
    user = request.user
    user_id = request.user.id

    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            example_instance = form.save(commit=False)
            example_instance.user = user
            example_instance.save()
            return HttpResponseRedirect(reverse('index'))            

    form = PasswordForm(initial={'user': request.user})
    password_data = Password_data.objects.filter(user_id=user_id)

    context = {
        'form': form,
        'password_data': password_data,
        'user': user
    }
    return render(request, "passwords/index.html", context)

def delete(request, id):
    password_data = Password_data.objects.get(pk=id)

    if request.method == 'POST':
        password_data.delete()

        return redirect('index')    

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'passwords/login.html', {
                'msg': 'Login failed'
            })
        
    return render(request, 'passwords/login.html')

def register_user(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'passwords/register.html', {
                'msg': 'Something went wrong during registration'
            })
    
    return render(request, "passwords/register.html", {"form": form})


def logout_user(request):
    logout(request)
    return render(request, 'passwords/login.html', {
        'msg': 'Logged out successfully'
    })
