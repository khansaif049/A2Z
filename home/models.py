from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=123, blank=True, default=None)
    email=models.CharField(max_length=123, blank=True, default=None)
    phone=models.CharField(max_length=123, blank=True, default=None)
    address=models.CharField(max_length=123, blank=True, default=None)
    times=models.CharField(max_length=123,null=True)
    Rail=models.CharField(max_length=123, blank=True, default=None)
    station=models.CharField(max_length=123, blank=True, default=None)
    locality=models.CharField(max_length=123, blank=True, default=None)
    work=models.CharField(max_length=123, blank=True, default=None)
    
    def __str__(self):
        return self.name

class detail(models.Model):
    firstname=models.CharField(max_length=123, blank=True, default=None)
    lastname=models.CharField(max_length=123, blank=True, default=None)
    phone=models.CharField(max_length=123, blank=True, default=None)

    def __str__(self):
        return self.firstname


