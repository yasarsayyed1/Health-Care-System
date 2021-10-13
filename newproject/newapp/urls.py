from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import Wellness,Cart,Orderview
from django.conf.urls.static import static

urlpatterns=[
    path("Home/",views.homeview,name="Home"),
    path("Signup/",views.signupview,name="signup"),
    path("login/",views.loginview,name="login"),
    path("logout/",views.logoutview,name="logout"),
    path("Ambulance/",views.ambulanceview,name="ambulance"),
    path("onway/",views.wayview,name="way"),
    path("data/",views.data,name="data"),
    path("appointment/",views.appointmentview,name="apo"),
    path("delete/<int:id>/",views.deleteview,name="dlt"),
    path("apointmentdata/",views.appointdataview,name="appointdata"),
    path("wellness/",Wellness.as_view(),name="wellness"),
    path("admin/",views.adminview,name="admin"),
    path("cart/",Cart.as_view(),name="cart"),
    #path("check-out",Checkout.as_view(),name="checkout"),
    path("paymentdone/",views.paymentdone,name="payment"),
    path("Order",Orderview.as_view(),name="order"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path("doctorform/", views.doctorformview, name="drform"),
    path("doctordata/", views.drdataview, name="drdata"),
    path("nursingform/", views.nursingformview, name="nurform"),
    path("nursingdata/", views.nursingdataview, name="nurdata"),
    path("roomserviceform/", views.roomserviceformview, name="rsform"),
    path("roomservicedata/", views.roomservicedata, name="rsdata"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

