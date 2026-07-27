from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib import messages
from django.urls import reverse

def login_view (request):

  if not request.user.is_authenticated:
    if request.method == 'POST':
      form = AuthenticationForm(request=request , data = request.POST )
      if form.is_valid():
        username =form.cleaned_data.get('username')
        password =form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')  #گرفتن مقصد قبلی
            if next_url:                         # اگر مقصد قبلی وجود داشت برش گردون همونجا
                return redirect(next_url)
            return redirect('website:index')
    
    form = AuthenticationForm()
    context = {'form':form}
    return render (request,'accounts/login.html',context)
  else:
    return redirect ('/')


def logout_view(request):
    if request.user.is_authenticated:
      logout(request)
    return redirect('/')

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You signed up successfully. Thank you.")
            return redirect('accounts:login')
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})