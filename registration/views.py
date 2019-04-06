import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import profile_form, LoginForm, RegisterForm
from .models import profile, Follower
from dal import autocomplete
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db import connection, IntegrityError
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from django import forms


def edit_profile(request):
    user = request.user

    form = profile_form(request.POST, request.FILES)

    if form.is_valid():

        profile = form.save(commit=False)
        profile.user = user
        profile.save()
        print("hello")
        return redirect(reverse('registration:show_profile'))



    else:
        form = profile_form()
        print("not hello")

    return render(request, 'registration/modify_profile.html', {"form": form})


def show_profile(request):
    user = request.user.id
    print(user)
    profile1 = get_object_or_404(profile, user=user)
    context = {
        "profile": profile1,
    }

    return render(request, 'registration/show_profile.html', context=context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:

            print(user.is_authenticated)
            login(request, user)
            return redirect(reverse('registration:show_profile'))
        else:
            print("User is none")

    return render(request, "registration/login.html", context=context)


def email_verify(form):
    rand_numb = random.randint(10000, 999999)
    global b
    b = str(rand_numb)
    email = [form.data['email']]
    response = send_mail("OTP for registration", b, "smarthealthcaresystemiiits@gmail.com", email)
    return b


# User = get_user_model()
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            b = email_verify(form)
            print(b)
            username = form.data['username']
            email = form.data['email']
            password = form.data['password']
            context = {
                'username': username,
                'email': email,
                'password': password,
                'b': b,
            }

            return render(request, 'registration/verify.html', context)
    else:
        form = RegisterForm()
        messages.error(request, 'Invalid login credentials')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


# User = get_user_model()
def new_user_reg(request):
    if b == request.POST['token']:
        if request.method == 'POST':
            username = request.POST.get('username', False)
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(request.POST['password'])
            new_user.save()
            login(request, new_user)
            print(new_user)
            return redirect('/users/edit_profile')
    else:
        return HttpResponse('Please give correct OTP')


def log_out(request):
    logout(request)

    return redirect('/')
