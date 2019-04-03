from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import story, comment
from .models import Blog, Comment, interest
from dal import autocomplete
from django.views.generic import RedirectView
import psycopg2
import datetime

# Create your views here.
from django.contrib.auth.models import User
def blog_display(request):
    user=request.user
    if request.method == 'POST':
        form = story(request.POST or None)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            interest = form.cleaned_data['interest']
            Blog.objects.create(author=user,heading=heading,content=form.cleaned_data['content'], interests=interest)
            return HttpResponse('Your story has been posted')

    else:
        context = {'form':story()}
        return render(request,'blog/form.html',context)

def home(request):
    user=request.user
    data=Blog.objects.all()
    conn = psycopg2.connect(host="localhost",database="blog", user="postgres", password="password")

    cur = conn.cursor()
    heading = 'about me and my blog'
    content = 'hdzb'
    now = datetime.datetime.now()
    i = interest.objects.get(interest_name='Health')
    cur.execute("SELECT author_id FROM blog_blog ORDER BY author_id")
    rows = cur.fetchall()
    # cur.execute("INSERT INTO blog_blog(author_id, heading,content,draft,post_date,interests_id) VALUES (%s,%s,%s,%s,%s,%s)", (user.id,heading,content,True,now,i.id))
    # conn.commit()
    # cur.execute("SELECT author_id FROM blog_blog ORDER BY author_id")
    # rows = cur.fetchall()
    print(rows)
    return render(request, 'home.html',{'data':data})

def show_blog(request, blog_id):
    user=request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    comments=Comment.objects.filter(blog_id=blog)

    if request.method == 'POST' and request.is_ajax:

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
            # return render(request,'blog.html',{'blog':blog , 'comments':comments,'form':comment()})
    return render(request, 'blog.html', {'blog': blog, 'comments':comments,'form':comment()})
class BlogLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        post_id=self.kwargs.get('blog_id')
        print(post_id)
        obj=get_object_or_404(Blog, pk=post_id)
        url = obj.get_absolute_url()
        user = self.request.user

        if user.is_authenticated:
            if user in obj.upvotes.all():
                obj.upvotes.remove(user)
            else:
                obj.upvotes.add(user)
        return url
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class BlogLikeAPI(APIView):


    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, blog_id=None, format=None):
        post_id=self.kwargs.get('blog_id')
        print(post_id)
        obj=get_object_or_404(Blog, pk=post_id)
        url = obj.get_absolute_url()
        upvotes_count=obj.upvotes.count()
        user = self.request.user
        updated= False
        liked= False
        if user.is_authenticated:
            if user in obj.upvotes.all():
                liked=False
                obj.upvotes.remove(user)
            else:
                liked=True
                obj.upvotes.add(user)
            updated=True
        data={
            "updated":updated,
            "liked":liked,
            "upvotes":upvotes_count
        }
        return Response(data)
class InterestAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = interest.objects.all()

        if self.q:
            qs = qs.filter(interest_name__istartswith=self.q)
        #print(qs)
        return qs
