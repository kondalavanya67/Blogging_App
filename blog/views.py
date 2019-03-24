from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import story, comment
from .models import Blog, Comment
# Create your views here.
from django.contrib.auth.models import User
def blog_display(request):
    user=request.user
    if request.method == 'POST':
        form = story(request.POST or None)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            Blog.objects.create(author=user,heading=heading,content=form.cleaned_data['content'])
            return HttpResponse('Your story has been posted')

    else:
        context = {'form':story()}
        return render(request,'blog/form.html',context)

def home(request):
    user=request.user
    data=Blog.objects.all()
    return render(request, 'home.html',{'data':data})

def show_blog(request, blog_id):
    user=request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    comments=Comment.objects.filter(blog_id=blog)
    if request.method == 'POST' and request.is_ajax:
        form = comment(request.POST or None)
        if form.is_valid():

            Comment.objects.create(blog_id=blog,author=user,content=form.cleaned_data['content'])
            comments=Comment.objects.filter(blog_id=blog)
            # return render(request,'blog.html',{'blog':blog , 'comments':comments,'form':comment()})
    return render(request, 'blog.html', {'blog': blog, 'comments':comments,'form':comment()})
