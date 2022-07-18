from product.models import Product
from django.contrib.auth.decorators import login_required


from http.client import HTTPResponse
from multiprocessing import context
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from cart.cart import Cart
from ordertable.models import Ordertable

# Create your views here.



def watch(request):
    product=Product.objects.all().order_by('-id')
    return render (request,'watches.html',{'products':product,'nbar': 'watch'})

def product(request,id):
    data=Product.objects.get(id=id)
    print(id)
    return render(request,"product.html",{'data':data})



def save(request):
    # print(request.POST)
    data=AppForm(request.POST,request.FILES)
    data.save()
    return redirect("/admin/create") 

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

def checkout(request):
    if request.method=="POST":
        phonenumber=request.POST.get('order_phonenumber')
        email=request.POST.get('order_emailorder_email')
        address=request.POST.get('order_address')
        pincode=request.POST.get('order_pincode')
        payment=request.POST.get('order_payment')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        
        for i in cart:
            a=(float(cart[i]['order_price']))
            b=cart[i]['order_quantity']
            total=a*b
            
            ordertable=Ordertable(
                user=user,
                productBrand=cart[i]['product_brand'],
                name=cart[i]['order_name'],
                price=cart[i]['order_price'],
                quantity=cart[i]['order_quantity'],
                image=cart[i]['order_image'],
                phonenumber=phonenumber,
                email=email,
                address=address,
                pincode=pincode,
                payment=payment,
                total=total,
            )
            order.save()
        request.session['cart']={}
        return redirect("/")

def order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(pk=uid)
    ordertable=Ordertable.objects.filter(user=user)

    return render(request, "checkout.html",{'ordertable':ordertable})