from django.contrib import admin
from .models import products,Friends,product_views

# Register your models here.
admin.site.register(products)
admin.site.register(Friends)
admin.site.register(product_views)