from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import requests
import json
from .models import Adminlogin,Merchentlogin,Product
import random
# Create your views here.
def Adminloginpage(request):
    return render(request,"adminlogin.html")


def logindetails(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    Adminlogin.objects.get(username=username,password=password)
    return render(request,"adminwelcome.html" )


def merchant(request):
    return render(request,"merchant.html")


def savemerchent(request):
    id=Merchentlogin.objects.values_list("merchentid")
    print(type(id))
    l=len(id)
    print(id)
    print(l)
    if(l!=0):
        r=id[l-1][0]+1
        print(r)
    else:

        r=1001
    merchantname=request.POST.get("m1")
    password=random.randint(10000,99999)
    emailid=request.POST.get("m2")
    contactno=request.POST.get("m3")
    Merchentlogin(merchentid=r,merchentname=merchantname,password=password,emailid=emailid,contactno=contactno).save()
    return render(request,"merchant.html",{"message":"merchent details are saved"})


def viewmerchent(request):

    return render(request,"viewmerchant.html",{"data":Merchentlogin.objects.all()})


def delete(request):
    id = request.GET.get("i")
    Merchentlogin.objects.filter(merchentid=id).delete()
    return render(request,"delete.html",{"data":Merchentlogin.objects.all()})
@method_decorator(csrf_exempt,name="dispatch")
class Merchentlog(View):
    def post(self,request,*args,**kwargs):
        mer=request.body
        data=json.loads(mer)
        print(data)
        m=Merchentlogin.objects.get(emailid=data['emailid'],contactno=data['contactno'])
        k=serialize('json',[m])
        print(k)
        return HttpResponse(k,content_type="j")

@method_decorator(csrf_exempt,name="dispatch")
class Productsave(View):
    def post(self,request,*args,**kwargs):
        y=request.body
        yy=json.loads(y)
        Product(productname=yy["productname"],productprice=yy["productprice"],merchantid=yy["merchantid"]).save()
        d={"mes":"data saved"}
        de=json.dumps(d)
        return HttpResponse(de,content_type="hghvhjg")


class Viewdata(View):
    def get(self,request):
        res=Product.objects.all()
        res1=serialize('json',res)
        return HttpResponse(res1,content_type="hguh")


class Update(View):
    def get(self,request,productid):
        print(productid)
        res = Product.objects.get(productid=productid)
        print(res)
        data = serialize('json',[res])

        return HttpResponse(data,status=200)
from django.forms.models import model_to_dict
from .forms import ProductForm
@method_decorator(csrf_exempt,name="dispatch")
class Saveupdate(View):
    def put(self,request,productid):
        print(productid)
        olddata=Product.objects.get(productid=productid)
        olddatadic=model_to_dict(olddata)
        # olddatadic=serialize('dict',[olddata])
        print(olddatadic)
        # olddatadic={"productid":olddata.productid,"productname":olddata.productname,"productprice":olddata.productprice,"merchantid":olddata.merchantid}
        newdata=request.body
        newdata1=json.loads(newdata)
        olddatadic.update(newdata1)

        #olddatadic.update(newdata1)
        print(olddatadic)
        f=ProductForm(olddatadic,instance=olddata)
        if f.is_valid():
            f.save()
        print(f)


        return HttpResponse(status=200)
        #
@method_decorator(csrf_exempt,name="dispatch")
class Delete(View):
    def delete(self,request,productid):
        Product.objects.get(productid=productid).delete()
        return HttpResponse(status=200)