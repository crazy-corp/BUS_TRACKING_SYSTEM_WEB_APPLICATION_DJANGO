from django.shortcuts import render,redirect
from SFE.models import sfed
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView , UpdateView ,DeleteView
# Create your views here. 
from django.http import HttpResponse
from django.http import FileResponse
from collections import OrderedDict
import os
import os.path
from os import path
import time
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy ,reverse
from .forms import addbusform
import requests  
import json

ar=list()
def my_view(request):
    return redirect('/sfe')


class addbus(CreateView):
    model = sfed
    form_class=addbusform
    #fields = ('Bus_ID','BusName',"Time")
    #template_name='post.html'
    #fields = '__all__'
    #success_url=reverse_lazy('article',args=(str(self.id))) ,args=(self.object.id,)
    def get_success_url(self):
        return reverse('SFE')


@csrf_exempt
def test(request):
    if request.method=="POST":
        print(request.POST)
        idd=request.POST.get("idd")
        print('POST', request.POST.get("idd"))
        cu=str(request.POST.get("current_status")).upper() + " @ " + str(request.POST.get("tim"))
        post=sfed.objects.filter(pk=idd).update(curr_s=cu)
        return HttpResponse("SUCCESS")
        #return render(request,'youtube/success.html')

# @csrf_exempt
# def test(request):
#     if request.method=="POST":
#         dt=dict(json.loads(request.body.decode("utf-8")))
#         print(dt["idd"])
#         # idd=request.POST.get("idd")
#         # print('POST', request.POST.get("idd"))
#         # cu=request.POST.get("current_status")
#         # post=sfed.objects.filter(pk=idd).update(curr_s=cu)
#         return render(request,'youtube/success.html')


@csrf_exempt
def sfe(request):
    #sfed(sfed=str("Trial"),date=timezone.now()).save()
    post=sfed.objects.all()
    print(post)
    for i in post:
        for j in dict(i.Sce):
            if j in ar:
                continue
            else:
                ar.append(j) 
    print(ar)
    #pagination
    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # bu=[]
    # bu_sce=[]
    # for i in post:
    #     bu.append([i.Bus_ID,i.BusName,i.curr_s])
    #     bu_sce.append((i.Bus_ID,i.Sce))
    #     #url=str(request.GET.get("url"))
    #     #links(links=url,date=timezone.now()).save()
    #     #return render(request,'categories.html',{'cat':cat,'category_posts':category_posts})
    # print(bu)
    # print(bu_sce)
    total=len(post)
    totalinp=len(post)
    return render(request,'SFE/table.html',{'ar':ar,'post':page_obj,'total':total,'totalinp':totalinp})
def scedule(request,ID):
    post=sfed.objects.filter(Bus_ID=ID)
    jo=post[0]
    post=dict(jo.Sce)
    curr=str(jo.curr_s)
    post= OrderedDict(sorted(post.items(), key=lambda kv:(kv[1], kv[0])))
    print(post)
    return render(request,'SFE/scedule.html',{'ar':ar,'post':post,'curr':curr})

@csrf_exempt
def searchresult(request):
    if request.method=="POST":
        fro=str(request.POST.get("from","")).upper()
        to=str(request.POST.get("to","")).upper()
        day=str(request.POST.get("day","")).upper()[0:2]
        print(day)
        post=sfed.objects.all()
        bu=[]
        for i in post:
            if fro in i.Sce:
                if to in i.Sce:
                    if(i.Sce[fro]<i.Sce[to]):
                        arr=str(i.days).split()
                        if(day in arr):
                            bu.append(i.Bus_ID)

        post2=[]
        for i in bu:
            post2.append(sfed.objects.filter(Bus_ID=int(i)))
    paginator = Paginator(post2, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total=len(post2)
    totalinp=len(page_obj)
        #print(post2[0][0].Bus_ID)
    return render(request,'SFE/searchresult.html',{'ar':ar,'post2':page_obj,'total':total,'totalinp':totalinp,'fro':fro,'to':to})