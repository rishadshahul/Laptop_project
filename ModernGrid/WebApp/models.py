from django.db import models

# Create your models here.


class useradmin(models.Model):
    username=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField(max_length=100, null=True,blank=True)
    password=models.CharField(max_length=100, null=True, blank=True)
    confirmpswd=models.CharField(max_length=100, null=True, blank=True)
