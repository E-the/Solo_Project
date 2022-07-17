from django.shortcuts import render,redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.



def watch(request):
    product=Product.objects.all().order_by('-id')
    return render (request,'watches.html',{'products':product,'nbar': 'watch'})

def product(request,id):
    data=Product.objects.get(id=id)
    print(id)
    return render(request,"product.html",{'data':data})

@login_required(login_url="/user/login")



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/product")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')