from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . import forms

# Profile view.
# Show the user's id/email/name.
def profile(request):
  if request.user.is_authenticated is False:
    return render(request, 'permissions_denied.html')

  id = request.user.id
  email = request.user.email
  username = request.user.get_full_name()
  if not username:
    username = request.user.username

  context = {
    'id' : id,
    'email' : email,
    'username' : username,
  }
  return render(request, 'registration/profile.html', context=context)