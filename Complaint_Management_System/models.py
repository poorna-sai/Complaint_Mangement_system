from statistics import mode
from django.db import models
from datetime import datetime  

# Create your models here.

class Complaints(models.Model):
    id_number=models.CharField(max_length=9)
    Name = models.CharField(max_length=50)
    complaint_txt = models.CharField(max_length=4000)
    Class = models.CharField(max_length =15,blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True )
    seen = models.BooleanField(default=False)
    department = models.CharField(max_length=30)
    videoproof = models.FileField(null=True, blank=True, upload_to = 'videos/')
    imageproof = models.ImageField(null=True , blank='True' , upload_to = 'images/')
    
    
class Solveddatabase(models.Model):
    id_number=models.CharField(max_length=9)
    Name = models.CharField(max_length=50)
    complaint_txt = models.CharField(max_length=4000)
    Class = models.CharField(max_length =15,blank=True)
    date = models.CharField(max_length=50)
    seen = models.BooleanField(default=False)
    department = models.CharField(max_length=30)
    videoproof = models.FileField(null=True, blank=True, upload_to = 'videos/')
    imageproof = models.ImageField(null=True , blank='True' , upload_to = 'images/')
    
    