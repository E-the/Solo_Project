from django.urls import path
from product import views

urlpatterns = [
    path("",views.watch),
    path('product/<int:id>',views.product),
    path('cart/<int:id>',views.cart)
]