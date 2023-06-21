from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.




def index(request):
    return render(request,'index.html')





def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps==cp:
                b = regmodel(name=cn,email=em, password=ps,mobile=mb,address=ad)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                nm = i.name
                if i.email == em and i.password == ps:
                    return render(request,'flipkartprofile.html',{'nm':nm})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'login.html')


def flipkartprofile(request):
    return render(request,'flipkartprofile.html')


def contact(request):
    return render(request,'contact.html')



def navbar(request):
    return render(request,'navbar.html')
