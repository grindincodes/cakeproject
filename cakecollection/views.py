from django.shortcuts import render
from .models import Content

def home(request):
    return render(request, 'cakecollection/home.html')

def new1(request):
    return render(request, 'cakecollection/new1.html')
def new2(request):
    return render(request, 'cakecollection/new2.html')
def new3(request):
    return render(request, 'cakecollection/new3.html')
def new4(request):
    return render(request, 'cakecollection/new4.html')

def mypage(request):
    posts=Content.objects.all()
    return render(request,'cakecollection/mypage.html',{'posts_list':posts})
    #mypage라는 함수 만들었고,
    #Content라는 모델에 가지고 오는 데이터베이스 데이터들을 posts에 담기
    #mypage.html에 posts_list라는 이름으로넘김(키:값)형태
# Create your views here.
