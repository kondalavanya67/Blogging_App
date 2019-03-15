from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import story
from .models import Blog
# Create your views here.
from django.contrib.auth.models import User
def blog_display(request):
    user = request.user
    if request.method == 'POST':
        form = story(request.POST or None)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            Blog.objects.create(author=user,heading=heading,content=form.cleaned_data['content'])
            return HttpResponse('Your story has been posted')

    else:
        context = {'form':story()}
        return render(request,'blog/form.html',context)


def create_story(request):
    return HttpResponse('Create Story HomePage')

