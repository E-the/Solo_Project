from django.shortcuts import render, redirect
from app.models import App
from app.forms import AppForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request,'index.html')


def about(request):
    items=App.objects.all()
    print(items)
    return render(request,'about.html', {'nbar': 'about'})

def main(request):
    items=App.objects.all()
    print(items)
    return render(request,'main.html', {'nbar': 'main'})

@login_required(login_url="/user/login")
def gallery(request):
    return render(request,'gallery.html')


def footer(request):
    return render(request,'footer.html')

@login_required(login_url="/user/login")
def features(request):
    return render(request,'features.html', {'nbar': 'features'})

def contact(request):
    return render(request,'contact.html', {'nbar': 'contact'})



@login_required(login_url="/user/login")
def create(request):
    return render(request, 'item/create.html')

def save(request):
    # print(request.POST)
    data=AppForm(request.POST,request.FILES)
    data.save()
    return redirect("/about") 

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