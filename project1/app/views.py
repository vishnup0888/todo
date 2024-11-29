from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
subject=[]
def index(request):
    if request.method=='POST':
        sub=request.POST['text']
        sub.append({'sub:sub'})
        return redirect(home)
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
