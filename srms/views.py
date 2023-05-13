from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth. models import User
from django.contrib import messages
import datetime
import requests
import re
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from student.models import*
from student.templates import*
# Create your views here.

def Home(request):
    data=className.objects.all()
    return render(request,"front_page.html",{'data':data})

