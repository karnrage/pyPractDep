# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


#did email, didn't do name

# Create your models here.

class BlogManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData["firstname"]) < 2:
            errors["firstname"] = "first name should be more than 1 character"
            # was name instead of first name length
        if len(postData["lastname"]) < 2:
            errors["lastname"] = "last name should be more than 1 character"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 character"
        if not re.match(EMAIL_REGEX, postData['emailreg']):
            errors["emailreg"] = ("invalid email")
        if not re.match(NAME_REGEX, postData['firstname']):
            errors["firstname"] = ("invalid first name")
        if not re.match(NAME_REGEX, postData['lastname']):
            errors["lastname"] = ("invalid last name")
        if User.objects.filter(email = postData ['emailreg']).exists():
            errors ['emailreg'] = "email already registered"
        
        return errors
        try:
            User.objects.get(email = postData['emailreg'])
            errors['emailreg'] = "The email is already taken"
        except:
            pass
        return
    def log_validator(self, postData): #need to finish
        errors = {}
        user = User.objects.get(email=postData['emaillog']) # models needs to be =postData, no request, because passing in variable of postdata
        #hashcheck = None python not needed?
        if len(postData['password']) < 8:
            errors["length"] = "password name should be more than 8 character"
            # was name instead of first name length
        if len(User.objects.filter(email = postData['emaillog'])) < 0:
            correct_user = User.objects.filter(email = postData["emaillog"])
        hash1 = bcrypt.checkpw(postData['password'].encode('utf8'), user.password.encode('utf8'))
        if hash1 == False:
            errors ['password'] = "Wrong password"
           # errors["email"] = "Blog name should be more than 1 character"
        # if type
        # if len(postData['desc']) < 10:
            # errors["desc"] = "Blog desc should be more than 10 characters"
        return errors

    # if (request.method == "POST")
    #     try:
    #         user = User.objects.get(email=rquest.POST['email'])
    # if(bcrypt.checkpw(request.POST['password'].encode('utf8'), User.password.encode('utf8'))):
    #     request.session['firstname'] = user.firstname
    #     request.session['firstname'] = user.firstname
    #     request.session['email'] = POST['email']
    #     request.session['id'] = user.id
    #     request.session['is-logged-in'] = True
    # else:
    #     messages.error(rquest, "wrong pass")
    #     return redirect("/")
    # else:
    #      return redirect("/")

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # confirm = models.CharField(max_length=255) #not needed cause only need to save password
    createdat = models.DateTimeField(auto_now_add = True)
    updatedat = models.DateTimeField(auto_now = True)
    objects = BlogManager()
    # age = models.IntegerField(default=70)
    # desc = models.TextField()

