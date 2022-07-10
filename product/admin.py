from django.contrib import admin
from product.models import Product





# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','watch_name','watch_price','watch_detail','watch_image')

admin.site.register(Product, ProductAdmin)
