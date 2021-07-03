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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cakecollection.views.home, name="home"),
    path('search/', cakecollection.views.home2, name="home2"),
    path('new/',cakecollection.views.new, name="new"),
    path('new2/', cakecollection.views.new2, name="new2"),
    path('new3/', cakecollection.views.new3, name="new3"),
    path('new4/', cakecollection.views.new4, name="new4"),
    path('new5/',cakecollection.views.new, name="new5"),
    path('new6/', cakecollection.views.new2, name="new6"),
    path('new7/', cakecollection.views.new3, name="new7"),
    path('new8/', cakecollection.views.new4, name="new8"),
    path('new9/', cakecollection.views.new4, name="new9"),
    path('mypage/',cakecollection.views.mypage, name="mypage"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)