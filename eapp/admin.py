from django.contrib import admin

# Register your models here.
from eapp.models import Product, Order

admin.site.register([Product, Order])
