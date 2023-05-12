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
    reg_date=models.TimeField(auto_created=True)

    



