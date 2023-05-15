from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth. models import User
from django.contrib import messages
from django.http.response import JsonResponse
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

csrf_exempt
def show_result(request):
    if request.method=="GET":
      email=request.GET.get('email')
      roll_no=request.GET.get('roll_no')
      class_name=request.GET.get('class_name')
      result_data=result.objects.all()
      data=[]
      for i in result_data:
         if (i.class_id.class_name)==class_name and (i.student_id.roll_no)==roll_no and (i.student_id.email)==email:
            data.append(i)

      student_name=""
      roll_no=""
      total_marks=0   
      result_status=False
      fullmarks=0
      percentage=0
      if( len(data)!=0):      
        for i in data:
           student_name=i.student_id.name 
           roll_no=i.student_id.roll_no
           total_marks=total_marks+int(i.marks)
           if int(i.marks)<=25:
              result_status=True

      if (len(data)!=0):
        fullmarks=len(data)*100
        percentage=(total_marks*100)/(fullmarks)
        percentage=round(percentage,2)

      percentage=str(percentage)
      return render(request,"show_result.html",{'class_name':class_name,'fullmarks':fullmarks,'data':data,'student_name':student_name,'roll_no':roll_no,'total_marks':total_marks,'percentage':percentage,'result_status':result_status})
    else:
       return HttpResponse("sorry server is down now")

def Feedback__(request,roll_no):
   return render(request,"Feedback.html",{'roll_no':roll_no})  

csrf_exempt
def Feedback_from(request,roll_no):
   if request.method=="POST":
     rating=request.POST.get('rating')
     Feedback_data=request.POST.get('Feedback_data')
     data=Feedback(
        Feedback_data=Feedback_data,
        rating=rating,
        roll_no=roll_no,
     )
     data.save()
     return render(request,"success.html")
   
def Reviews__(request,roll_no):
   return render(request,"Reviews.html",{'roll_no':roll_no})  


csrf_exempt
def Reviews_from(request,roll_no):
   if request.method=="POST":
     Reviews_data=request.POST.get('Reviews_data')
     data=Reviews(
        Reviews_data=Reviews_data,
        roll_no=roll_no,
     )
     data.save()
   return render(request,"success.html")

