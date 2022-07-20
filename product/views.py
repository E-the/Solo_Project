from product.models import Product
from django.contrib.auth.decorators import login_required


from http.client import HTTPResponse
from multiprocessing import context
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from cart.cart import Cart
from orders.models import Order

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
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        payment=request.POST.get('payment')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        
        for i in cart:
            a=(float(cart[i]['price']))
            b=cart[i]['quantity']
            total=a*b
            
            order=Order(
                user=user,
                name=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
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
    order=Order.objects.filter(user=user)
    return render(request, "checkout.html",{'order':order})


def search(request):
    query=request.GET['query']
    product = Product.objects.filter(watch_name__icontains=query)
    return render(request, 'searchresults.html' ,{'product': product})
    