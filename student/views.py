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

def manage_reviews(request):
    data=Reviews.objects.all()
    return render(request,"manage_reviews.html",{'data':data})

def delete_Reviews(request,Reviews_id):
     data=Reviews.objects.get(Reviews_id=Reviews_id)
     data.delete()
     return redirect('/adminpanel/manage_reviews')

def manage_feedback(request):
    data=Feedback.objects.all()
    return render(request,"manage_feedback.html",{'data':data})

def delete_feedback(request,Feedback_id):
    data=Feedback.objects.get(Feedback_id=Feedback_id)
    data.delete()
    return redirect('/adminpanel/manage_feedback')

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
    class_data=className.objects.all()
    student_data=student.objects.all()
    subject_data=subjects.objects.all()
    result_data=result.objects.all()
    total_reviews=Reviews.objects.all()
    total_feedback=Feedback.objects.all()
    set1 = set()
    for i in result_data:
        set1.add(i.student_id.student_id)    
    set2=set()
    for i in set1:
        for j in result_data:
            if(j.student_id.student_id)==i :
                if int(j.marks)<=25:
                    set2.add(i)
    print(len(class_data))                   
    context={
        'total_class':len(class_data),
        'total_student':len(student_data),
        'total_subject':len(subject_data),
        'Total_result':len(set1),
        'Total_pass_candidates':len(set1)-len(set2),
        'Total_XP_candidates':len(set2),
        'total_reviews':len(total_reviews),
        'total_feedback':len(total_feedback),

    }
    return render(request, "dashboard.html",context)    

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
        class_name_numeric=request.POST.get('class_name_numeric')
        error_mess=[]
        class_data=className.objects.all()
        count=0
        for i in class_data:
            if (i.class_name==class_name) or (i.class_name_numeric==class_name_numeric):
                count+=1
                error_mess.append("Invalid Data")
        if count:
            return render(request,"manage_Add_class.html",{'error':error_mess})
        else:            
            data=className(
                class_name=class_name,
                class_name_numeric=class_name_numeric,
            )
            data.save()
            return redirect('/adminpanel/manageclass')
    return HttpResponse("Wait sometime")

def manageclass_search_class_id(request):
    if request.method=="GET":
        class_id=request.GET.get('class_id')
        classNamedata=className.objects.all()
        data=[]
        for i in classNamedata:
            if str(i.class_id)==str(class_id):
                data.append(i)
        return render(request,"Manage_class.html",{'data':data})
    
def manageclass_search_class_name(request):
    if request.method=="GET":
        class_name=request.GET.get('class_name')
        classNamedata=className.objects.all()
        data=[]
        for i in classNamedata:
            if str(i.class_name)==str(class_name):
                data.append(i)
        return render(request,"Manage_class.html",{'data':data})

def manageclass_search_class_name_numeric(request):
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
        class_name_numeric=request.POST.get('class_name_numeric')
        data=className.objects.get(class_id=class_id)   
        if data:
            data.class_name=class_name
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
        error=[]
        count=0
        student_data=student.objects.all()
        # for i in student_data:
        #     if str(i.email)==str(email):
        #         count+=1
        #         error.append("This mail id is already exit !!")
        #         break
        for i in student_data:
            if str(i.class_id.class_name)==str(class_id) and str(i.roll_no)==str(roll_no):
                 count+=1
                 error.append("This roll number is already exit !!") 
                 break
        if count!=0:
            data=className.objects.all()
            return render(request,"manage_student_add.html",{'data':data,'error':error})
        else:
            for i in data:
                s=""
                s=s+str(i.class_name)
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
        subject_data=subjects.objects.all()
        error=[]
        count=0
        for i in subject_data:
            if i.subject_name==subject_name or i.subject_code==subject_code:
                count+=1
                error.append("subject_name or subject_code is already use")
        if count:
            return render(request,"subject/manage_subject_add.html",{'error':error})
        else:               
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

def delete_subject_com(request,subject_com_id):
    data=subject_com.objects.get(subject_com_id=subject_com_id)
    data.delete()
    return redirect('/adminpanel/manage_subject_com')

def manage_add_subject_com(request):
    class_data=className.objects.all()
    subject_data=subjects.objects.all()
    return render(request,"subject_com/manage_subject_com_add.html",{'class_data':class_data,'subject_data':subject_data})

def manage_com_search_subject_com_id(request):
    if request.method=="GET":
        subject_com_id=request.GET.get('subject_com_id')
        subject_com_data=subject_com.objects.all()
        data=[]
        for i in subject_com_data:
            if str(i.subject_com_id)==str(subject_com_id):
                data.append(i)       
        return render(request,"subject_com/manage_subject_com.html",{'data':data})

def manage_com_search_class_name(request):
    if request.method=="GET":
        class_name=request.GET.get('class_name')
        subject_com_data=subject_com.objects.all()
        data=[]
        for i in subject_com_data:
            if str(i.class_id.class_name)==str(class_name):
                data.append(i)        
        return render(request,"subject_com/manage_subject_com.html",{'data':data})

def manage_com_search_subject_name(request):
    if request.method=="GET":
        subject_name=request.GET.get('subject_name')
        subject_com_data=subject_com.objects.all()
        data=[]
        for i in subject_com_data:
            if str(i.subject_id.subject_name)==str(subject_name):
                data.append(i)        
        return render(request,"subject_com/manage_subject_com.html",{'data':data})    

def subject_com_submit_data(request):
    if request.method=="POST":
        class_name=request.POST.get('class_name')
        subject_name=request.POST.get('subject_name')
        class_data=className.objects.get(class_name=class_name)
        class_id=class_data.class_id
        subject_data=subjects.objects.get(subject_name=subject_name)
        subject_id=subject_data.subject_id
        data=subject_com(
            class_id=className.objects.get(class_id=class_id),
            subject_id=subjects.objects.get(subject_id=subject_id)
        )
        data.save()
        return redirect('/adminpanel/manage_subject_com')

#manage_result
def manage_result(request):
    data=result.objects.all()
    return render(request,"result/manage_result.html",{'data':data})

def addresult(request):
    class_data=className.objects.all()
    return render(request,"result/manage_result_add.html",{'class_data':class_data})

def search_class_name_to_add(request):
    if request.method=="POST":
        class_name=request.POST.get('class_name')
        class_data=className.objects.get(class_name=class_name)
        student_data=student.objects.filter(class_id=class_data.class_id)
        subject_data=subject_com.objects.filter(class_id=class_data.class_id)
        
        return render(request,"result/manage_result_add_adv.html",{'class_name':class_name,'student_data':student_data,'subject_data':subject_data})
    else:return HttpResponse("Wait sometime")

def delete_result(request,result_id):
    data=result.objects.get(result_id=result_id)
    data.delete()
    return redirect('/adminpanel/manage_result')
@csrf_exempt
def manage_result_add_data(request,class_name):
    if request.method=="POST":
        roll_no=request.POST.get('roll_no')
        result_data=result.objects.all()
        count=0
        for i in result_data:
            if str(i.class_id.class_name)==str(class_name) and str(i.student_id.roll_no)==str(roll_no):
                count+=1
                break
        if count!=0:
            return HttpResponse("This result is already exit")
        else:
            class_data=className.objects.get(class_name=class_name)
            subject_data=subject_com.objects.filter(class_id=class_data.class_id)
            for i in subject_data:
                s=i.subject_id.subject_name
                s2=request.POST.get(s)
                id=0
                student_data=student.objects.all()
                for i in student_data:
                    if str(i.class_id.class_name)==str(class_name) and str(i.roll_no)==str(roll_no):
                        id=i
                data=result(
                    class_id=className.objects.get(class_name=class_name),
                    student_id=id,
                    marks=s2,
                    subject_id=subjects.objects.get(subject_name=s)
                )
                data.save()
            return redirect('/adminpanel/manage_result')
    return HttpResponse("Hello World!")

def manage_result_search_result_id(request):
    if request.method=="GET":
        result_id=request.GET.get('result_id')
        result_data=result.objects.all()
        data=[]
        for i in result_data:
            if str(i.result_id)==str(result_id):
                data.append(i)       
        return render(request,"result/manage_result.html",{'data':data})
    
def manage_result_search_student_name(request):
    if request.method=="GET":
        student_name=request.GET.get('student_name')
        result_data=result.objects.all()
        data=[]
        for i in result_data:
            if str(i.student_id.name)==str(student_name):
                data.append(i)       
        return render(request,"result/manage_result.html",{'data':data})

def manage_result_search_class_name(request):
    if request.method=="GET":
        class_name=request.GET.get('class_name')
        result_data=result.objects.all()
        data=[]
        for i in result_data:
            if str(i.class_id.class_name)==str(class_name):
                data.append(i)       
        return render(request,"result/manage_result.html",{'data':data})    
    
def manage_result_search_subject_name(request):
    if request.method=="GET":
        subject_name=request.GET.get('subject_name')
        result_data=result.objects.all()
        data=[]
        for i in result_data:
            if str(i.subject_id.subject_name)==str(subject_name):
                data.append(i)       
        return render(request,"result/manage_result.html",{'data':data}) 

def manage_result_search_roll_no(request):
    if request.method=="GET":
        roll_no=request.GET.get('roll_no')
        result_data=result.objects.all()
        data=[]
        for i in result_data:
            if str(i.student_id.roll_no)==str(roll_no):
                data.append(i)       
        return render(request,"result/manage_result.html",{'data':data})           
def manage_result_search_marks(request):
    if request.method=="GET":
        marks=request.GET.get('marks')
        result_data=result.objects.all()
        data=[]
        for i in result_data:
            if str(i.marks)==str(marks):
                data.append(i)       
        return render(request,"result/manage_result.html",{'data':data})    

def update_result(request,result_id):
    data=result.objects.get(result_id=result_id)
    return render(request,"result/manage_result_update.html",{'data':data})

def manage_update_submit(request,result_id):
    if request.method=="POST":
        data=result.objects.get(result_id=result_id)
        marks=request.POST.get('marks')
        data.marks=marks
        data.save()
    return redirect('/adminpanel/manage_result')


def search_top_candidates(request):
    data=className.objects.all()
    return render(request,"search_top_candidates.html",{'data':data})

def search_class_name_to_find_top_candidates(request):
    if request.method=="POST":
        class_name=request.POST.get('class_name')
        data=[]
        result_data=result.objects.all()
        student_data=student.objects.all()
        mp = {}
        for i in student_data:
            for j in result_data:
                if str(i.roll_no)==str(j.student_id.roll_no) and str(class_name)==str(j.class_id.class_name):
                    if j in mp:
                        mp[j]=mp[j]+int(j.marks)
                    else:
                        mp[j]=int(j.marks) 
        for i in mp:
            print(i)                  
    return HttpResponse("EHHE")