# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import User
import bcrypt
# needed to import User object from models file


def index(request):
    response = "Hello, I am your first request!"
    users = User.objects.all()
    context = {
        'users': users
    }
  # return HttpResponse(response)
    return render(request, 'logreg_app/index.html', context)



def create(request):
    errors = User.objects.reg_validator(request.POST)
    if len (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['emailreg']
        password = request.POST['password']
        confirm = request.POST['confirm']
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())           
        person = User.objects.create(firstname=firstname, lastname=lastname, email=email, password=hashed)#need to pass in hashed password into database
        request.session["id"] = person.id
        person.save()
        print "registrant was created"
        return redirect("/success") # do not render to POST, could get lost in loop
    #now redirct to route that handles sucess page 
    # return redirect('/')

def login(request):
    errors = User.objects.log_validator(request.POST)
    user = User.objects.get(email=request.POST['emaillog'])
    if len (errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect( "/")
    else:
        bcrypt.checkpw('password'.encode('utf8'), user.password.encode('utf8'))
        request.session['id'] = user.id

        return redirect( "/success")
        # changed to redirect because 
    #errors = Users.objects.login_validator(request.POST)
    #password = request.post['password']

def success(request): #request is default parameter
    users = User.objects.all()
    context = {
        'users': User.objects.get(id=request.session['id'])
    }
    
    return render (request, "logreg_app/success.html", context) 

def logout(request):
    request.session.clear()
    return redirect('/')

