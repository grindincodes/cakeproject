"""ideaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import cakecollection.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cakecollection.views.home,name="home"),
    path('new1/', cakecollection.views.new1, name="new1"),
    path('new2/', cakecollection.views.new2, name="new2"),
    path('new3/', cakecollection.views.new3, name="new3"),
    path('new4/', cakecollection.views.new4, name="new4"),
    path('mypage/',cakecollection.views.mypage, name="mypage"),

]
