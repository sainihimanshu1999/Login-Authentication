from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import the UserLoginForm, UserRegisterForm

