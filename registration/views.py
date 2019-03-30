from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import profile_form
from .models import profile,Follower
from dal import autocomplete
from django.views.generic import RedirectView
from django.contrib.auth.models import User


def edit_profile(request):
    user = request.user
    if request.method=="POST":

        form=profile_form(request.POST, request.FILES ,initial={'user':user})

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=user
            profile.save()

            return redirect(reverse('registration:edit_profile'))

    else:
        form=profile_form(initial={'user':user})
    return render(request,'registration/modify_profile.html',{'form':form})



def show_profile(request):
    user = request.user
    profile = profile.objects.get(user=user)
    context={
         'profile':profile
    }
    return render(request, 'registration/show_profile.html', context=context)
   



   
