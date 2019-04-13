import random
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import profile_form, LoginForm, RegisterForm
from .models import profile,Follower
from dal import autocomplete
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db import connection,IntegrityError
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django import forms
import psycopg2
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

conn=psycopg2.connect(host="127.0.0.1", database="blog", user="postgres", password="kalpa@123")



@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



def edit_profile(request):
    user = request.user

    form=profile_form(request.POST, request.FILES)
    

    if form.is_valid():

        user_data=form.cleaned_data
        curr = conn.cursor()
        curr.execute("INSERT INTO registration_profile (user_id, fullname,gender, age,phone_no) VALUES (%d, %s, %s, %s,%s)",(user.id ,user_data['fullname'], user_data["gender"], user_data["age"],user_data["phone_no"]))

        conn.commit()
        return redirect(reverse('registration:show_profile'))       

    else:
        form=profile_form()

    return render(request,'registration/modify_profile.html',{"form":form})

  


def show_profile(request):
    user = request.user
    user_id=user.id
    curr = conn.cursor()
    curr.execute("SELECT * FROM registration_profile WHERE user_id= %s", [user_id])
    row=curr.fetchone()
    print(row)
    return render(request,'registration/show_profile.html', {'profile':row })
   

def login_page(request):

    form=LoginForm(request.POST or None)
    context= {
       "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            print(user.is_authenticated)
            login(request, user)
            return redirect(reverse('registration:show_profile'))
        else:
            print("User is none")

    return render(request, "registration/login.html", context=context)

def email_verify(form):
    rand_numb=random.randint(10000, 999999)
    global b
    b=str(rand_numb)
    email=[form.data['email']]
    response=send_mail("OTP for registration",b,"smarthealthcaresystemiiits@gmail.com",email)
    return b

#User = get_user_model()
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            b=email_verify(form)
            print(b)
            username=form.data['username']
            email=form.data['email']
            password=form.data['password']
            context={
            'username':username,
            'email':email,
            'password':password,
            'b':b,
            }

            return render(request,'registration/verify.html', context)
    else:
        form=RegisterForm()
        messages.error(request, 'Invalid login credentials')
    context={
    'form':form
    }
    return render(request,'registration/register.html',context)

#User = get_user_model()
def new_user_reg(request):
    if b == request.POST['token']:
        if request.method =='POST':
            username=request.POST.get('username',False)
            email=request.POST.get('email',False)
            password=request.POST.get('password',False)
            new_user=User.objects.create(username=username,email=email)
            new_user.set_password(request.POST['password'])
            new_user.save()
            login(request,new_user)
            print(new_user)
            return redirect('/users/edit_profile')
    else:
        return HttpResponse('Please give correct OTP')



def log_out(request):
    logout(request)

    return redirect('/')


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
