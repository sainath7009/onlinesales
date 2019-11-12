import random

from django.shortcuts import render, redirect
from .models import MerchentModel

def adminlogin(request):
    return render(request,"loginpage.html")


def homepage(request):
    if request.POST['un']=="sai":
        if request.POST['ups']=="sai":
            return render(request,"home.html")
        else:
            return render(request,"loginpage.html",{"error":"Invalid password "})
    else:
        return render(request, "loginpage.html", {"error1": "Invalid user "})


def adminlogout(request):
    return adminlogin(request)


def merchentpage(request):
    auto = 0
    try:
        var = MerchentModel.objects.all()[::-1][0]
        auto = int(var.m_idno)+ 1
    except IndexError:
        auto = 1500
    return render(request,"merchentpage.html",{"data":MerchentModel.objects.all(),"key":auto})


def savemerchent(request):
    id=request.POST['idno']
    name=request.POST['na']
    cno=request.POST['cno']
    email=request.POST['email']
    #pw=request.POST['ps']
    pw=random.randint(100000,999999)
    MerchentModel(m_name=name,m_contact=cno,m_email=email,m_password=pw,m_idno=id).save()
    return merchentpage(request)
