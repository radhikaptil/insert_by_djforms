from django.db import models

# Create your models here.
class Student(models.Model):
    Sname=models.CharField(max_length=10)
    Sid=models.IntegerField()
    Sage=models.IntegerField()
    Semail=models.EmailField()
    