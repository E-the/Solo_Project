from django.shortcuts import render
from product.models import Product

# Create your views here.


def watch(request):
    product=Product.objects.all()
    return render (request,'watches.html',{'products':product})

def product(request,id):
    data=Product.objects.get(id=id)
    print(id)
    return render(request,"product.html",{'data':data})

def cart(request,id):
    data=Product.objects.get(id=id)
    return render(request,"cart.html",{'data':data})