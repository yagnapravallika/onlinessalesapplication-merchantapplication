from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
# Create your views here.
def merchantlogin(request):
    return render(request,"merchantlogin.html")


def savedetails(request):
    emailid=request.POST.get("t1")
    contactno=request.POST.get("t2")
    d={"emailid":emailid,"contactno":contactno}
    data1=json.dumps(d)
    print(data1)
    res=requests.post("http://127.0.0.1:8000/merchant/",data=data1)
    print(res)
    print(res.status_code)
    print(res.json())
    return render(request,"mer.html",{"data":res.json()})


def addproduct(request):
    return render(request,"add.html")


def addsave(request):
    producname=request.POST.get("t1")
    productprice=request.POST.get("t2")
    merchantid=request.POST.get("t3")
    add={"productname":producname,"productprice":productprice,"merchantid":merchantid}
    add1=json.dumps(add)
    kk=requests.post("http://127.0.0.1:8000/addd/",data=add1)
    print(kk.status_code)
    print(kk.json())
    return render(request,"datasaved.html")


def viewdata(request):
    k=requests.get("http://127.0.0.1:8000/viewdata/")
    return render(request,"viewdata.html",{"data":k.json()})


def update1(request):
    productid=request.GET['productid']
    print(productid)
    res = requests.get("http://127.0.0.1:8000/update/" + productid + "/")
    print(res)
    print(res.json())
    if res.status_code==200:
        return render(request,"add.html",{"data":res.json()})
    else:
        return HttpResponse('ok')


def updatesave(request):
    productid=request.POST.get("t1")
    productname=request.POST.get("t2")
    productprice=request.POST.get("t3")
    data1={"productname":productname,"productprice":productprice}
    data2=json.dumps(data1)
    print(data2)
    yy=requests.put("http://127.0.0.1:8000/saveupdate/"+productid+"/",data=data2)
    if yy.status_code==200:
        return render(request,"dataupdated.html",{"data":"data updated"})


def deletedata(request):
    productid=request.GET["productid"]
    yy=requests.delete("http://127.0.0.1:8000/deletee/"+productid+"/")

    return render(request,"delete.html",{"data":"data deleted"})