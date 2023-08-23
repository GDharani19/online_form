from django.shortcuts import render
from feedback.forms import feedbackform
from feedback.models import feedbackmodel
from django.http import HttpResponse
# Create your views here.

def createfeed(request):
    form=feedbackform()
    if request.method=="POST":
        form=feedbackform(request.POST)
        form.save()
        return HttpResponse("data is stored")
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
