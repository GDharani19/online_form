from django.shortcuts import render,redirect
from feedback.forms import feedbackform
from feedback.models import feedbackmodel
from django.http import HttpResponse

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.

def createfeed(request):
    form=feedbackform()
    if request.method=="POST":
        form=feedbackform(request.POST)
        # form.save()
        subject = 'welcome to ITCTRLS world'
        message = f'Hi {request.POST.get("Name")}, thank you for registering in ITCTRLS Technologies.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get('Email'), ]
        send_mail(subject, message, email_from, recipient_list )
        print("haii")
        return redirect("/feedback/read/")
    return render(request,"homepage.html",{"form":form})

def readfeed(request):
    res=feedbackmodel.objects.all()
    return render(request,'details.html',{"res":res})

def updatefeed(request,pk):
    res = feedbackmodel.objects.get(id=pk)
    form = feedbackform(instance=res)
    if request.method =='POST':
        res=feedbackmodel.objects.get(id=pk)
        form = feedbackform(request.POST,instance=res)
        form.save()
        return HttpResponse("Data is stored")
    return render(request,"homepage.html",{'form':form})

def deletefeed(request,pk):
    res = feedbackmodel.objects.get(id=pk)
    if request.method =='POST':
        res=feedbackmodel.objects.get(id=pk).delete()
        return HttpResponse("Data is deleted")
    return render(request,"delete_confirm.html",{'res':res})

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]

        user=User.objects.create_user(
            username=username,
            password=password,
            email=email
        )


        login(request,user)
        subject = 'welcome to ITCTRLS world'
        message = f'Hi {User.username}, thank you for registering in ITCTRLS Technologies.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [User.email, ]
        send_mail(subject, message, email_from, recipient_list )
        return redirect("/dashboard/")
    return render(request,"signup.html")
