from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings

qua=(("BHMS","BHMS"),('BAMS','BAMS'),('MBBS','MBBS'),('Physiotherapists','Physiotherapists'),('MD',"MD"))
gen=(('male','male'),('famale','female'))
qu=(('BSC Nursing','BSC Nursing'),('Graduation+Nursing Cource','Graduation+Nursing Cource'))

# Create your models here.
class Ambulancemodel(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_age=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=12)
    location=models.CharField(max_length=30)
    disease=models.CharField(max_length=40)
class Appointmentmodel(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    previous_visit=models.CharField(max_length=30)
    if_before_visited_visit_detail=models.CharField(max_length=30)
    appointment_date=models.DateField()
    slot=models.CharField(max_length=30)

class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='newapp/images',default="")
    def __str__(self):
        return self.name

class Drformmodel(models.Model):
    name=models.CharField(max_length=30)
    gender = models.CharField(max_length=30,choices=gen,default='2')
    address=models.CharField(max_length=50,default='')
    age=models.IntegerField()
    qualification=models.CharField(max_length=30,choices=qua)

class Nursingmodel(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=gen)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=30, choices=qu)

class Roomservicemodel(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, choices=gen)
    address = models.CharField(max_length=50)
    age = models.IntegerField()


class Ordersmodel(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default='-',blank=True)
    phone_number=models.CharField(max_length=12,default='-',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    def placeorder(self):
        self.save()
