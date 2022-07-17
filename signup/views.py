from django.shortcuts import render, redirect
from signup.models import Signup
from signup.form import SignupForm
from django.contrib.auth.decorators import login_required
# Create your views here.






def signup(request,id):
    # items=Signup.objects.all()
    data=Signup.objects.get(id=id)
    form=SignupForm(request.POST,request.FILES,instance=data)
    form.save()
    return render(request,"new/signup.html",{'data':data})
    

@login_required(login_url="/user/login")
def data(request):
    items=Signup.objects.all()
    return render(request, 'new/data.html', {'items':items,'nbar': 'data'})

def user(request):
    # print(request.POST)
    data=SignupForm(request.POST)
    data.save()
    return redirect("/signup/data") 





# Create your views here.
