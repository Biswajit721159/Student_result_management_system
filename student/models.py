from django.db import models

class className(models.Model):
    class_id=models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    class_name_numeric=models.CharField(max_length=100)

class student(models.Model):
    student_id=models.AutoField(primary_key=True)
    class_id=models.ForeignKey(className,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gendar=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    reg_date=models.TimeField(auto_now_add=True)
    
class subjects(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=100)
    subject_code=models.CharField(max_length=100) 

class subject_com(models.Model):
    subject_com_id=models.AutoField(primary_key=True)
    class_id=models.ForeignKey(className,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)

class result(models.Model):
    result_id=models.AutoField(primary_key=True)    
    class_id=models.ForeignKey(className,on_delete=models.CASCADE)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    marks=models.CharField(max_length=100)

class Feedback(models.Model):
    Feedback_id=models.AutoField(primary_key=True)
    roll_no=models.CharField(max_length=100)
    Feedback_data=models.CharField(max_length=500)
    rating=models.CharField(max_length=100)
 
