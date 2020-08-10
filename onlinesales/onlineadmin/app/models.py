from django.db import models

class Adminlogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Merchentlogin(models.Model):
    merchentid=models.IntegerField(primary_key=True)
    merchentname=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    emailid=models.EmailField(unique=True)
    contactno=models.IntegerField(unique=True)
class Product(models.Model):
    productid=models.AutoField(primary_key=True)
    productname=models.CharField(max_length=30)
    productprice=models.FloatField()
    merchantid=models.IntegerField()

