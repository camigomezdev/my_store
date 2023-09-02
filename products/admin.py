from django.contrib import admin
from .models import Product, Brand, Comment

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Comment)