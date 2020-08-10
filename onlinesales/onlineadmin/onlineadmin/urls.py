"""onlineadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Adminloginpage,name="admin"),
    path("logindetails/",views.logindetails,name="logindetails"),
    path("merchentdetails/",views.merchant,name="merchant"),
    path("savemerchent/",views.savemerchent,name="savemerchent"),
    path("viewmerchent/",views.viewmerchent,name="viewmerchent"),
    path("delete/",views.delete,name="delete"),

    path('merchant/',views.Merchentlog.as_view()),
    path("addd/",views.Productsave.as_view()),
    path("viewdata/",views.Viewdata.as_view()),
    path('update/<int:productid>/',views.Update.as_view()),
    path("saveupdate/<int:productid>/",views.Saveupdate.as_view()),
    path("deletee/<int:productid>/",views.Delete.as_view())
]
