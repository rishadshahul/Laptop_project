from django.db import models

# Create your models here.


class categoryDB(models.Model):
    cateName=models.CharField(max_length=100,null=True,blank=True)
    cateImage=models.ImageField(upload_to="profile")


class productdb(models.Model):
    ProductName = models.CharField(max_length=30, null=True, blank=True)
    ProductCategory = models.CharField(max_length=30, null=True, blank=True)
    ProductPrice = models.IntegerField(null=True, blank=True)
    ProductDescription = models.CharField(max_length=1500, null=True, blank=True)
    ProductQuantity = models.IntegerField(null=True, blank=True)
    ProductImage = models.ImageField(upload_to="profile")


class ContactDB(models.Model):
    message=models.CharField(max_length=500, null=True, blank=True)
    Cname=models.CharField(max_length=100, null=True, blank=True)
    Cemail=models.EmailField(max_length=100, null=True, blank=True)
    Csubject=models.CharField(max_length=100, null=True, blank=True)














# class productDB(models.Model):
#     ProName=models.CharField(max_length=100,null=True,blank=True)
#     Procate=models.CharField(max_length=100,null=True,blank=True)
#     ProPrice=models.IntegerField(null=True,blank=True)
#     ProDescription=models.CharField(max_length=1000,null=True,blank=True)
#     ProQuantity=models.IntegerField(null=True,blank=True)
#     ProImage=models.ImageField(upload_to="profile")

# class productDB2(models.Model):
    # ProName = models.CharField(max_length=100, null=True, blank=True)
    # ProductCategory = models.CharField(max_length=100, null=True, blank=True)
    # ProPrice = models.IntegerField(null=True, blank=True)
    # ProDescription = models.CharField(max_length=1000, null=True, blank=True)
    # ProQuantity = models.IntegerField(null=True, blank=True)
    # ProImage = models.ImageField(upload_to="profile")



    
  






