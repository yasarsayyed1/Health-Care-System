import django_filters
from .models import *

class Productfilter(django_filters.FilterSet):
    class Meta:
        model=Product
        fields=['name','price']