from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render,redirect
import os
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
from bookwebsite.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate
import time
import datetime

from datetime import timedelta
from django .views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

# Create your views here.


class userregister(generic.CreateView):
    form_class = userregisterform
    template_name = 'userregister.html'
    success_url = reverse_lazy('userlogin')

class userlogin(generic.View):
    form_class=userloginform
    template_name = 'userlogin.html'
    def get(self,request):
        form =self.form_class
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        if request.method == 'POST':
            a= userloginform(request.POST)
            if a.is_valid():
                us= a.cleaned_data["username"]
                ps= a.cleaned_data["password"]
                b= User.objects.all()
                for i in b:
                    if us == i.username and ps == i.password:
                        return redirect(home)
                return HttpResponse("failed")
            return HttpResponse("invalid")

def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,'home.html')


class bookupload(generic.CreateView):
    form_class = bookform
    template_name = 'bookupload.html'
    success_url = reverse_lazy('bookupload')
    def get(self,request):
        a=bookmodel.objects.all()
        bookname=[]
        bookpdf=[]
        bookimage=[]
        author=[]
        bookdate=[]
        id1=[]
        for i in a:
            bkn=i.bookname
            bookname.append(bkn)
            bkpdf=str(i.bookpdf).split('/')[-1]
            bookpdf.append(bkpdf)
            bkimg=str(i.bookimage).split('/')[-1]
            bookimage.append(bkimg)
            authr=i.author
            author.append(authr)
            bkdt=i.bookdate
            bookdate.append(bkdt)
            id=i.id
            id1.append(id)
        mylist=zip(bookname,bookpdf,bookimage,author,bookdate,id1)
        return render(request,self.template_name,{"mylist":mylist})


class bookdelete(generic.DeleteView):
    model = bookmodel
    template_name = 'delete.html'
    success_url = reverse_lazy('bookupload')

class bookedit(generic.UpdateView):
    model = bookmodel
    template_name = 'bookupdate.html'
    form_class = bookform
    fields = '__all__'
    def get(self,request,**kwargs):
        id1=kwargs.get('pk')
        a=self.model.objects.get(id=id1)
        bookname=a.bookname
        bookpdf=str(a.bookpdf).split('/')[-1]
        bookimage=str(a.bookimage).split('/')[-1]
        author=a.author
        bookdate=a.bookdate
        return render(request,self.template_name,{"bookname":bookname,"bookpdf":bookpdf,"bookimage":bookimage,"author":author,"bookdate":bookdate})
    def post(self, request, **kwargs):
        idee=kwargs.get('pk')
        a=self.model.objects.get(id=idee)
        if request.method=='POST':
            if len(request.FILES):
                if len(a.bookpdf)>0:
                    os.remove(a.bookpdf.path)
                a.bookpdf=request.FILES['bookpdf']
                if len(a.bookimage)>0:
                    os.remove(a.bookimage.path)
                a.bookimage=request.FILES['bookimage']
            a.bookname=request.POST.get('bookname')
            a.author=request.POST.get('author')
            a.bookdate=request.POST.get('bookdate')
            a.save()
            return redirect('http://127.0.0.1:8000/bookapp/bookupload')
        return render(request,self.template_name,{"a":a})

class bookdownloads(generic.ListView):
    model = bookmodel
    template_name = 'bookdownload.html'


    def get(self,request):
        bookname=[]
        bookpdf=[]
        a=self.model.objects.all()
        for i in a:

            bkname=i.bookname
            bookname.append(bkname)
            bkpdf=str(i.bookpdf).split('/')[-1]
            bookpdf.append(bkpdf)
        mylist=zip(bookname,bookpdf)
        return render(request,self.template_name,{"mylist":mylist})


class bookllogoutview(LogoutView):
    next_page = reverse_lazy('userlogin')




