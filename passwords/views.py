from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')

    form = PasswordForm()
    password_data = Password.objects.all()

    context = {
        'form': form,
        'password_data': password_data
    }

    return render(request, "passwords/index.html", context)

def delete(request, id):
    password_data = Password.objects.get(pk=id)

    if request.method == 'POST':
        password_data.delete()

        return redirect('index')    
