from django.shortcuts import render, redirect
from app.models import App
from app.forms import AppForm
from django.contrib import messages
from .models import Feedback
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.


def index(request):
    return render(request,'index.html')

def error(request):
    return render(request,'404.html')


def about(request):
    items=App.objects.all()
    print(items)
    return render(request,'about.html', {'nbar': 'about'})


def main(request):
    items = Product.objects.filter(product_catog='apple').values().order_by('-id')[0:4]
    samsung = Product.objects.filter(product_catog='samsung').values().order_by('-id')[0:4]
    print(items)
    return render(request,'main.html', {'items':items,'samsung':samsung, 'nbar': 'main'})

@login_required(login_url="/user/login")
def gallery(request):
    return render(request,'gallery.html')


def footer(request):
    return render(request,'footer.html')

@login_required(login_url="/user/login")
def features(request):
    return render(request,'features.html', {'nbar': 'features'})


def contact(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        email = data['email']
        feedback = data['feedback']
        user_feedback = Feedback.objects.create(name=name,
                                                email=email,
                                                feedback=feedback)
        if user_feedback:
            messages.success(request, 'Feedback submitted. Thank You!')
        else:
            messages.error(request, "Error in submitting. Please try again")

    context = {
        'contact': 'active',
    }
    return render(request, 'contact.html', context )
    







def back(request):
    return redirect("/create")  
    # return render(request,'index.html')



def edit(request,id):
    data=App.objects.get(id=id)
    print(id)
    return render(request,"item/edit.html",{'data':data})

def update(request,id):
    data=App.objects.get(id=id)
    form=AppForm(request.POST,request.FILES,instance=data)
    form.save()
    return redirect("/watches")

# def delete(request,id):
#     data=App.objects.get(id=id)
#     data.delete()
#     return redirect("/about")

