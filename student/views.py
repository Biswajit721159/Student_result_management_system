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
from .models import*
# Create your views here.


def index(request):
    return render(request, "Admin_login.html")


@csrf_exempt
def connect(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/adminpanel/dashboard')
        else:
            error_mess=[]
            error_mess.append("Invalid Username or Password")
            return render(request,"Admin_login.html",{'error':error_mess})
    else:
        return HttpResponse("Something is wrong")
    
def dashboard(request):
    return render(request, "dashboard.html")    

def Logout(request):
    logout(request)
    return redirect('/adminpanel/logoutpage')

def logoutpage(request):
    return render(request,"logoutpage.html")



#manageclass

def manageclass(request):
    data=className.objects.all()
    return render(request,"Manage_class.html",{'data':data})

def addclass(request):
    return render(request,"manage_Add_class.html")

def submit_data(request):
    if request.method=="POST":
        class_name=request.POST.get('class_name')
        section=request.POST.get('section')
        class_name_numeric=request.POST.get('class_name_numeric')
        data=className(
            class_name=class_name,
            section=section,
            class_name_numeric=class_name_numeric,
        )
        data.save()
        return redirect('/adminpanel/manageclass')
    return HttpResponse("Wait sometime")

def manage_search_class_id(request):
    if request.method=="GET":
        class_id=request.GET.get('class_id')
        classNamedata=className.objects.all()
        data=[]
        for i in classNamedata:
            if str(i.class_id)==str(class_id):
                data.append(i)
        return render(request,"Manage_class.html",{'data':data})
    
def manage_search_class_name(request):
    if request.method=="GET":
        class_name=request.GET.get('class_name')
        classNamedata=className.objects.all()
        data=[]
        for i in classNamedata:
            if str(i.class_name)==str(class_name):
                data.append(i)
        return render(request,"Manage_class.html",{'data':data})

def manage_search_section(request):
    if request.method=="GET":
        section=request.GET.get('section')
        classNamedata=className.objects.all()
        data=[]
        for i in classNamedata:
            if str(i.section)==str(section):
                data.append(i)
        return render(request,"Manage_class.html",{'data':data})

def manage_search_class_name_numeric(request):
    if request.method=="GET":
        class_name_numeric=request.GET.get('class_name_numeric')
        classNamedata=className.objects.all()
        data=[]
        for i in classNamedata:
            if str(i.class_name_numeric)==str(class_name_numeric):
                data.append(i)
        return render(request,"Manage_class.html",{'data':data})            
    
def class_update(request,class_id):
    data=className.objects.get(class_id=class_id)
    return render(request,"manage_class_update.html",{'data':data})

def class_delete(request,class_id):
    data=className.objects.get(class_id=class_id)
    data.delete()
    return redirect('/adminpanel/manageclass')
    
def manage_class_submit_updated_data(request,class_id):
    if request.method=="POST":

        class_name=request.POST.get('class_name')
        section=request.POST.get('section')
        class_name_numeric=request.POST.get('class_name_numeric')
        data=className.objects.get(class_id=class_id)   
        if data:
            data.class_name=class_name
            data.section=section
            data.class_name_numeric=class_name_numeric
            data.save()
            return redirect('/adminpanel/manageclass')
        else:
            return HttpResponse("We Find Some Error")

