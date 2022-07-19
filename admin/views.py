from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import *
from user.models import *
from product.forms import ProductForm
from product.models import *
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout




# Create your views here.


# def message_page(request):
#     message = MessageModel.objects.all()
#     return render(request,'admin/message.html',{'message':message})

@login_required(login_url="/admin/login")
def user_display(request):
    users = User.objects.exclude(username=request.user.username)
    context = {
        "all_users": users,
    }
    return render(request, 'admin/allusers.html', context)

@login_required(login_url="/admin/login")
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/admin/allusers')

def change_to_admin(request, username):
    user_data = User.objects.filter(username=username)
    user_data.update(is_staff=True)
    return redirect('/admin/allusers')


def remove_from_admin(request, username):
    user_data = User.objects.filter(username=username)
    user_data.update(is_staff=False)
    return redirect('/admin/allusers')

def login_page(request):
    return render(request,'admin/admin_login.html' , {'nbar': 'main'})

@login_required(login_url="/admin/login")
def create(request):
    return render(request, 'admin/create.html' , {'nbar': 'add'})

@login_required(login_url="/admin/login")
def contact(request):
    feedback = Feedback.objects.all().order_by('date_posted')
    context = {
        "all_feedback": feedback
    }
    return render(request, 'admin/admin_contact.html', context)
    # return render(request, 'admin/admin_contact.html' , {'nbar': 'contact'})


def feedback_details(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    context = {
        'feedback': feedback
    }
    return render(request, 'admin/feedback.html', context)


def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_superuser == 1:
                log(request,user)
                return redirect('/admin/admin_home')

            else:

                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/admin/login')

        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")
            return redirect('/admin/login')

    else:
        messages.error(request,"Something is worng with your form validation, Please Try Again !")
        return redirect('admin/login')

def add(request):
    data = ProductForm(request.POST, request.FILES)
    print(request.POST)
    data.save()
    return redirect('/admin/admin_home')

def edit(request,id):
    data=Product.objects.get(id=id)
    return render(request, "admin/adminedit.html",{'data':data})   

def delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect("/admin/admin_home")

def updatepage(request,id):
    data=Product.objects.get(id=id)
    form=ProductForm(request.POST,request.FILES,instance=data)
    form.save()
    return redirect("/admin/admin_home")

def log_out(request):
    logout(request)
    return redirect('admin/login')

def admin_home(request):
    products=Product.objects.all().order_by('-id')
    return render (request,'admin/adminhome.html',{'products': products, 'nbar': 'main'})

    

 
    


