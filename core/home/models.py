from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100);
    age=models.IntegerField(max_length=3);
    name=models.EmailField(max_length=100);
    name=models.TextField(max_length=100);
    name=models.ImageField();
    name=models.FileField();
