from django.contrib import admin
from .models import Ambulancemodel,Appointmentmodel,Product,Category,Drformmodel,Nursingmodel,Roomservicemodel,Ordersmodel
# Register your models here.
class Adminambulance(admin.ModelAdmin):
    list_display = ['patient_name','patient_age','contact_number','location','disease']
admin.site.register(Ambulancemodel,Adminambulance)

class AdminAppoint(admin.ModelAdmin):
    list_display = ['name','gender','city','previous_visit','if_before_visited_visit_detail','appointment_date','slot']
admin.site.register(Appointmentmodel,AdminAppoint)


class Productadmin(admin.ModelAdmin):
    list_display = ['name','price','description','category']
admin.site.register(Product,Productadmin)

class Categoryadmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,Categoryadmin)

class Drformmodeladmin(admin.ModelAdmin):
    list_display = ['name','gender','address','qualification']
admin.site.register(Drformmodel,Drformmodeladmin)

class Nursingmodeladmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'address', 'qualification']
admin.site.register(Nursingmodel,Nursingmodeladmin)

class Roomservicemodeladmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'address']
admin.site.register(Roomservicemodel,Roomservicemodeladmin)

class Ordersmodeladmin(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','address','phone_number','date']
admin.site.register(Ordersmodel,Ordersmodeladmin)
