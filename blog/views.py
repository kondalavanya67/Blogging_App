from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
# Create your views here.

def create_story(request):
    return HttpResponse('Create Story HomePage')
