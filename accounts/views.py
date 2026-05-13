from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm

def register(request):
    if request.user.is_authenticated:
        return redirect('website:home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('website:home')
    else:
        form = UserRegistrationForm()
    return render(request,"registration/signup.html",{"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('website:home')
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = request.POST.get('username'),
                password = request.POST.get('password')
            )
            if user is not None:
                login(request,user)
                return redirect('website:home')
    else:
        form = AuthenticationForm()
    return render(
        request,
        "registration/login.html",
        {"form": form}
    )

def logout_view(request):
    logout(request)
    return redirect('accounts:login')