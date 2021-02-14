from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
import os

from .forms import (
    LoginForm,
    RegisterForm,
    UserUpdateForm
)

User = get_user_model()


# Create your views here.
def register_view(request):
  if request.user.is_authenticated:
    return redirect('items')

  form = RegisterForm(request.POST or None)

  if form.is_valid():
    username = form.cleaned_data.get('username')
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password1')
    password2 = form.cleaned_data.get('password2')

    try:
      user = User.objects.create_user(username, email, password)
    except:
      user = None

    if user != None:
      # request.user == user
      # login(request, user)
      messages.success(
          request, 'Your account has been created! You can login now!')
      return redirect('login')
    else:
      request.session['register_error'] = 1
      # return render(request, "recipe/list.html", {'form': form, 'invalid_user': True})

  return render(request, "accounts/forms.html", {'form': form, 'title': 'Join Today'})


def login_view(request):
  if request.user.is_authenticated:
    return redirect('items')

  next_redirect = request.GET.get('next')
  form = LoginForm(request.POST or None)

  if form.is_valid():
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(request, username=username, password=password)

    if user != None:
      # request.user == user
      login(request, user)
      return redirect('items')
    else:
      # attempt = request.session.get("attempt") or 0
      # request.session['attempt'] += 1
      # return redirect("/invalid-password")
      request.session['invalid_user'] = 1
      # return render(request, "recipe/list.html", {'form': form, 'invalid_user': True})

  return render(request, "accounts/forms.html", {'form': form, 'title': 'Log In'})


def logout_view(request):
  logout(request)
  return redirect('login')
