from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request,'first_app/index.html',{'users': User.objects.get()})

def login_fun(request):
    errors = User.objects.login_manager(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_firstname']= user.first_name
        request.session['user_lastname']= user.last_name
        request.session['user_email']= user.email

    return redirect ('/login')

def login(request):
    return render (request, 'first_app/login.html', {'users': User.objects.get()})

def logout(request):
    request.session.clear()
    return redirect ('/')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    hash_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.create( first_name= request.POST['first_name'],last_name= request.POST['last_name'],email= request.POST['email'], password= hash_pass )
    return redirect('/login/'+str(user.id))
    