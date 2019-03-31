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
    #print(comments.first().id)
    if request.method == 'POST':
        form = comment(request.POST or None)
        if form.is_valid():
            p = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                qs = Comment.objects.filter(id=parent_id)
                if qs.count!=0:
                    p = qs.first()
            Comment.objects.create(blog_id=blog,author=user,content=form.cleaned_data['content'],parent=p)
            comments=Comment.objects.filter(blog_id=blog)
            return render(request,'blog.html',{'blog':blog , 'comments':comments,'form':comment()})
    return render(request, 'blog.html', {'blog': blog, 'comments':comments,'form':comment()})
