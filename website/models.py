from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    rating = models.IntegerField()
    decsription = models.CharField(max_length=500)
    
        

class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    phone_number = models.IntegerField()
    
    

class Branches(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    
    
class Employees(models.Model):
    full_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=60)
    sex = models.CharField(max_length=20)
