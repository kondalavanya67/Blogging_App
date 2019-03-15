from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
# Create your views here.

def blog_display(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'blog/form.html',{})


def create_story(request):
    return HttpResponse('Create Story HomePage')

