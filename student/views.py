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

#managestudent

def managestudent(request):
    data=student.objects.all()
    return render(request,"manage_student.html",{'data':data})

def addstudent(request):
    data=className.objects.all()
    return render(request,"manage_student_add.html",{'data':data})

def student_submit_data(request):
    if request.method=="POST":
        class_id=request.POST.get('class_id')
        name=request.POST.get('name')
        roll_no=request.POST.get('roll_no')
        email=request.POST.get('email')
        gendar=request.POST.get('gendar')
        dob=request.POST.get('dob')
        new_class_id=0
        data=className.objects.all()
        for i in data:
            s=""
            s=s+str(i.class_name)
            s=s+"-"
            s=s+str(i.section)
            if s==class_id:
                new_class_id=i.class_id
        data=student(
            class_id=className.objects.get(class_id=new_class_id),
            name=name,
            roll_no=roll_no,
            email=email,
            gendar=gendar,
            dob=dob
        )  
        data.save()      
        return redirect('/adminpanel/managestudent')
    else:return HttpResponse("please wait")

def delete_student(request,student_id):
    data=student.objects.get(student_id=student_id)
    data.delete()
    return  redirect('/adminpanel/managestudent')   

def update_student(request,student_id):
    data=student.objects.get(student_id=student_id)
    return render(request,"manage_student_update.html",{'data':data})

def update_student_submit_data(request,student_id):
    if request.method=="POST":
        name=request.POST.get('name')
        roll_no=request.POST.get('roll_no')
        email=request.POST.get('email')
        gendar=request.POST.get('gendar')
        dob=request.POST.get('dob')
        data=student.objects.get(student_id=student_id)
        data.name=name
        data.roll_no=roll_no
        data.email=email
        data.gendar=gendar
        data.dob=dob
        data.save()
        return redirect('/adminpanel/managestudent')
    return HttpResponse("Wait for responce")

def manage_search_student_id(request):
    if request.method=="GET":
        student_id=request.GET.get('student_id')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            if str(i.student_id)==str(student_id):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})
    
def manage_search_class_name(request):
    if request.method=="GET":
        class_id=request.GET.get('class_name')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            s=""
            s=s+str(i.class_id.class_name)
            s=s+"-"
            s=s+str(i.class_id.section)
            if s==str(class_id):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})
    
def manage_search_name(request):
    if request.method=="GET":
        name=request.GET.get('name')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            if str(i.name)==str(name):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})

def manage_search_roll_no(request):
    if request.method=="GET":
        roll_no=request.GET.get('roll_no')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            if str(i.roll_no)==str(roll_no):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})

def manage_search_email(request):
    if request.method=="GET":
        email=request.GET.get('email')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            if str(i.email)==str(email):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})

def manage_search_gendar(request):
    if request.method=="GET":
        gendar=request.GET.get('gendar')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            if str(i.gendar)==str(gendar):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})

def manage_search_dob(request):
    if request.method=="GET":
        dob=request.GET.get('dob')
        all_data=student.objects.all()
        data=[]
        for i in all_data:
            if str(i.dob)==str(dob):
                data.append(i)
        return render(request,"manage_student.html",{'data':data})  

#managesubject

def managesubject(request):
    data=subjects.objects.all()
    return render(request,"subject/manage_subject.html",{'data':data})        

def subject_search_subject_id(request):
    if request.method=="GET":
       subject_id=request.GET.get('subject_id')
       all_data=subjects.objects.all()
       data=[]
       for i in all_data:
           if str(i.subject_id)==str(subject_id):
               data.append(i)
       return render(request,"subject/manage_subject.html",{'data':data})        
    else: return HttpResponse("please wait some Time")       

def subject_search_subject_name(request):
    if request.method=="GET":
       subject_name=request.GET.get('subject_name')
       all_data=subjects.objects.all()
       data=[]
       for i in all_data:
           if str(i.subject_name)==str(subject_name):
               data.append(i)
       return render(request,"subject/manage_subject.html",{'data':data})        
    else: return HttpResponse("please wait some Time")       

def subject_search_subject_code(request):
    if request.method=="GET":
       subject_code=request.GET.get('subject_code')
       all_data=subjects.objects.all()
       data=[]
       for i in all_data:
           if str(i.subject_code)==str(subject_code):
               data.append(i)
       return render(request,"subject/manage_subject.html",{'data':data})        
    else: return HttpResponse("please wait some Time")       
    
def delete_subject(request,subject_id):
    data=subjects.objects.get(subject_id=subject_id)
    data.delete()
    return redirect('/adminpanel/managesubject')

def add_subject(request):
    return render(request,"subject/manage_subject_add.html")

def subject_submit_data(request):
    if request.method=="POST":
        subject_name=request.POST.get('subject_name')
        subject_code=request.POST.get('subject_code')
        data=subjects(
            subject_name=subject_name,
            subject_code=subject_code
        )
        data.save()
        return redirect('/adminpanel/managesubject')
    return HttpResponse("Wait for Responce")

def subject_update_data(request,subject_id):
    data=subjects.objects.get(subject_id=subject_id)
    return render(request,"subject/manage_subject_update.html",{'data':data})

def submit_subject_updated_data(request,subject_id):
    if request.method=="POST":
        subject_name=request.POST.get('subject_name')
        subject_code=request.POST.get('subject_code')
        data=subjects.objects.get(subject_id=subject_id)
        data.subject_code=subject_code
        data.subject_name=subject_name
        data.save()
        return redirect('/adminpanel/managesubject')
    return HttpResponse("Wait for Responce")

#manage_subject_com

def manage_subject_com(request):
    data=subject_com.objects.all()
    return render(request,"subject_com/manage_subject_com.html",{'data':data})