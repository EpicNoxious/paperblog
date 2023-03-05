from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def loginUser(request):
  page = 'login'
  form = CustomUserLoginForm()
  if request.method == 'POST':
    form = CustomUserLoginForm(data=request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist')
    
    if form.is_valid():
      user = form.get_user()
      if user is not None:
        login(request, user)
        messages.error(request, 'user has logged in')
        return redirect('index')
      else:
        messages.error(request, 'username or password is incorrect')
      # login(request, user)
      # messages.success(request, "User logged in")
      # return redirect('index')
    else:
      form = CustomUserLoginForm()
  context = {'page': page, 'form': form}
  return render(request, 'signupin.html', context)




def logoutUser(request):
  logout(request)
  messages.info(request, 'user was logged out')
  return redirect('index')


def registerUser(request):
  page = 'register'
  form = CustomUserCreationForm()
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=True)
      
      messages.success(request, 'User account was created!')

      login(request, user)
      return redirect('login')
    else:
      messages.error(request, 'An error occurred during registeration')
  context = {'page': page, 'form': form}
  return render(request, 'signupin.html', context)