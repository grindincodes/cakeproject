
from django.shortcuts import render, redirect
from .models import Content
from .forms import ContentForm

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
def new(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new.html', {'form':form})
def new2(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new2.html', {'form':form})
def new3(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new3.html', {'form':form})

def new4(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new4.html', {'form':form})

def new5(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new5.html', {'form':form})

def new6(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new6.html', {'form':form})

def new7(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new7.html', {'form':form})
def new8(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new8.html', {'form':form})

def new9(request):
    if request.method=='POST':
        form=ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')#자기 주문내역 확인하기
    else:
        form=ContentForm()

    return render(request, 'cakecollection/new9.html', {'form':form})