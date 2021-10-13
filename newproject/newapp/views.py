from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from .forms import Userform,Ambulaceform,Appointmentform,Doctorform,Nursingform,Roomserviceform
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from .models import Ambulancemodel,Appointmentmodel,Product,Category,Drformmodel,Nursingmodel,Roomservicemodel,Ordersmodel
from django.conf import settings
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth.models import User
from .middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from .filters import Productfilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def homeview(request):
    temp_name="newapp/Home.html"
    context={}
    return render(request,temp_name,context)

def signupview(request):
    form=Userform()
    if request.method=="POST":
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            i=form.cleaned_data['email']
            subject = 'welcome to the Helathify'
            message = 'Hi,thank you for registering in Healthify.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list =[i]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('login')
    temp_name="newapp/signup.html"
    context={'form':form}
    return render(request,temp_name,context)

def loginview(request):
    if request.method=="POST":
        i=request.POST.get('ua')
        n=request.POST.get('pa')
        user=authenticate(username=i,password=n)
        if user != None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,'invalid credentials')
    temp_name="newapp/login.html"
    context={}
    return render(request,temp_name,context)

def logoutview(request):
    request.session.clear()
    logout(request)
    return redirect('login')

def ambulanceview(request):
    form=Ambulaceform()
    if request.method=="POST":
        form=Ambulaceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('way')
    temp_name="newapp/Ambulance.html"
    context={"form":form}
    return render(request,temp_name,context)

def wayview(request):
    temp_name="newapp/onway.html"
    context={}
    return render(request,temp_name,context)

def data(request):
    data=Ambulancemodel.objects.all()
    temp_name="newapp/ambulancedata.html"
    context={"data":data}
    return  render(request,temp_name,context)

def appointmentview(request):
    form=Appointmentform()
    if request.method=="POST":
        form=Appointmentform(request.POST)
        if form.is_valid():
            i=form.cleaned_data['name']
            n=form.cleaned_data['gender']
            m=form.cleaned_data['city']
            o=form.cleaned_data['Have_you_previously_attended_facility']
            p=form.cleaned_data['if_yes_state_on_which_condition_and_when']
            q=form.cleaned_data['please_select_appointment_date']
            r=form.cleaned_data['slot']
            appoint=Appointmentmodel(name=i,gender=n,city=m,previous_visit=o,if_before_visited_visit_detail=p,appointment_date=q,slot=r)
            appoint.save()
            return redirect('Home')
    temp_name="newapp/Appointments.html"
    context={"form":form}
    return render(request,temp_name,context)
def deleteview(request,id):
    user=Ambulancemodel.objects.get(id=id)
    user.delete()
    return redirect('data')
def appointdataview(request):
    data=Appointmentmodel.objects.all()
    temp_name="newapp/appointmentdata.html"
    context={"data":data}
    return render(request,temp_name,context)

class Wellness(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        cat = Category.objects.all()
        cat_id = request.GET.get('category')
        if cat_id:
            product = Product.objects.filter(category=cat_id)
        else:
            product = Product.objects.all()
        myfilter = Productfilter(request.GET, queryset=product)
        product = myfilter.qs

       #paginator

        # page_number = request.GET.get('page')
        # try:
        #     page_obj = p.get_page(page_number)  # returns the desired page object
        # except PageNotAnInteger:
        #     if page_number is not an integer then assign the first page
            # page_obj = p.page(1)
        # except EmptyPage:
        #     if page is empty then return last page
            # page_obj = p.page(p.num_pages)
        temp_name = "newapp/wellness.html"
        context = {"product": product, 'cat': cat,'myfilter':myfilter}
        return render(request, temp_name, context)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')#by using session accesing cart
        if cart:#if product is already there then incrementing and not there then upending
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart:-',request.session['cart']) #adding to session again because we made change in session
        return redirect('wellness')


def adminview(request):
    temp_name="newapp/admin.html"
    context={}
    return render(request,temp_name,context)

def doctorformview(request):
    form=Doctorform()
    if request.method=="POST":
        form=Doctorform(request.POST)
        form.save()
        return redirect('drdata')
    temp_name="newapp/doctorform.html"
    context={"form":form}
    return render(request,temp_name,context)

def drdataview(request):
    data=Drformmodel.objects.all()
    temp_name="newapp/drdata.html"
    context={'data':data}
    return render(request,temp_name,context)

def nursingformview(request):
    form=Nursingform()
    if request.method=="POST":
        form=Nursingform(request.POST)
        form.save()
        return redirect('nurdata')
    temp_name="newapp/nursingform.html"
    context={'form':form}
    return render(request,temp_name,context)

def nursingdataview(request):
    data=Nursingmodel.objects.all()
    temp_name="newapp/nursingdata.html"
    context={"data":data}
    return render(request,temp_name,context)

def roomserviceformview(request):
    form=Roomserviceform()
    if request.method=="POST":
        form=Roomserviceform(request.POST)
        form.save()
        return redirect('rsdata')
    temp_name="newapp/rsform.html"
    context={"form":form}
    return render(request,temp_name,context)

def roomservicedata(request):
    data=Roomservicemodel.objects.all()
    temp_name="newapp/rsdata.html"
    context={"data":data}
    return render(request,temp_name,context)


class Cart(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        product=Product.objects.filter(id__in=ids)
        temp_name="newapp/cart.html"
        context={"product":product}
        return render(request,temp_name,context)


def paymentdone(request):
    if request.method=="POST":
        customer = request.user
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        products=Product.objects.filter(id__in=ids)
        for product in products:
            order=Ordersmodel(customer=customer,
                          product=product,
                          price=product.price,
                          address=address,
                          phone_number=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('order')




    # def post(self, request):
    #     address = request.POST.get('address')
    #     phone = request.POST.get('phone')
    #     customer=request.user
    #     cart=request.session.get('cart')
    #     ids = list(request.session.get('cart').keys())
    #     products=Product.objects.filter(id__in=ids)
    #     for product in products:
    #         order=Ordersmodel(customer=customer,
    #                           product=product,
    #                           price=product.price,
    #                           address=address,
    #                           phone_number=phone,
    #                           quantity=cart.get(str(product.id)))
    #         order.save()
    #     request.session['cart'] = {}
    #     return redirect('order')


# class Checkout(View):
#     def post(self,request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer=request.user
#         cart=request.session.get('cart')
#         ids = list(request.session.get('cart').keys())
#         products=Product.objects.filter(id__in=ids)
#         for product in products:
#             order=Ordersmodel(customer=customer,
#                               product=product,
#                               price=product.price,
#                               address=address,
#                               phone_number=phone,
#                               quantity=cart.get(str(product.id)))
#             order.save()
#         return redirect('payment')




# def payview(request):
#     ids = list(request.session.get('cart').keys())
#     product = Product.objects.filter(id__in=ids)
#     if request.method=="POST":
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.user
#         cart = request.session.get('cart')
#         for product in product:
#             order = Ordersmodel(customer=customer,
#                                     product=product,
#                                     price=product.price,
#                                     address=address,
#                                     phone_number=phone,
#                                     quantity=cart.get(str(product.id)))
#             order.save()
#             return redirect('Home')
#         request.session['cart'] = {}
#     temp_name = "newapp/payment.html"
#     context = {"product":product}
#     return render(request,temp_name,context)


class Orderview(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.user
        order=Ordersmodel.objects.filter(customer=customer).order_by('-date')
        temp_name = 'newapp/order.html'
        context={"order":order}
        return render(request,temp_name,context)