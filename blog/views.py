from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import story, comment
from .models import Blog, Comment, interest
from dal import autocomplete
from django.views.generic import RedirectView
from rest_framework import status
import psycopg2
import datetime

conn = psycopg2.connect(host="127.0.0.1", database="blog", user="postgres", password="password")
# Create your views here.
from django.contrib.auth.models import User


def blog_display(request):
    user = request.user
    if request.method == 'POST':
        form = story(request.POST or None)
        if form.is_valid():
            heading = form.cleaned_data['heading']
            interest = form.cleaned_data['interest']
            content = form.cleaned_data['content']
            '''Creating a blog'''
            # Blog.objects.create(author=user,heading=heading,content=form.cleaned_data['content'], interests=interest)
            now = datetime.datetime.now()
            cur = conn.cursor()
            cur.execute("INSERT INTO blog_blog(author_id, heading,content,draft,post_date,interests_id) VALUES "
                        "(%s,%s,%s,%s,%s,%s)", (user.id, heading, content, True, now, interest.id))
            conn.commit()
            return HttpResponse('Your story has been posted')

    else:
        context = {'form': story()}
        return render(request, 'blog/form.html', context)


def home(request):
    user = request.user
    '''getting all objects of blog'''
    # data=Blog.objects.all()
    cur = conn.cursor()
    cur.execute("SELECT * FROM blog_blog ORDER BY post_date")
    rows = cur.fetchall()
    return render(request, 'home.html', {'data': rows})


def show_blog(request, blog_id):
    user = request.user
    '''Getting object with id'''
    blog1 = get_object_or_404(Blog, pk=blog_id)
    cur = conn.cursor()
    cur.execute("SELECT * FROM blog_blog WHERE id=" + str(blog_id))
    blog = cur.fetchone()
    print(blog)
    comments = Comment.objects.filter(blog_id=blog[0])
    var = "SELECT * FROM blog_comment WHERE blog_id_id=" + str(blog[0])
    cur.execute(var)
    rows = cur.fetchall()
    print(rows)
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
                if qs.count != 0:
                    p = qs.first()
            '''Creating Comment'''
            # Comment.objects.create(blog_id=blog[0],author=user,content=form.cleaned_data['content'],parent=p)
            cur = conn.cursor()
            now = datetime.datetime.now()
            cur.execute("INSERT INTO blog_comment(blog_id_id,author_id, content,parent_id,timestamp) VALUES "
                        "(%s,%s,%s,%s,%s)", (blog[0], user.id, form.cleaned_data['content'], parent_id, now))
            conn.commit()

            comments = Comment.objects.filter(blog_id=blog[0])
            # return render(request,'blog.html',{'blog':blog , 'comments':comments,'form':comment()})
    return render(request, 'blog.html', {'blog': blog, 'comments': comments, 'form': comment(), 'blog1': blog1})


class BlogLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        post_id = self.kwargs.get('blog_id')
        print(post_id)
        obj = get_object_or_404(Blog, pk=post_id)
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
from blog.serializer import BlogSerializer
from blog.serializer import interestSerializer


class BlogLikeAPI(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, blog_id=None, format=None):
        post_id = self.kwargs.get('blog_id')
        print(post_id)
        obj = get_object_or_404(Blog, pk=post_id)
        url = obj.get_absolute_url()
        cur = conn.cursor()

        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.upvotes.all():
                liked = False
                # obj.upvotes.remove(user)
                cur = conn.cursor()
                '''Deleting from upvotes'''
                cur.execute('DELETE FROM blog_blog_upvotes WHERE user_id=' + str(user.id))
                conn.commit()
            else:
                liked = True
                '''Adding a upvote using many to many '''
                # obj.upvotes.add(user)
                cur = conn.cursor()
                cur.execute('INSERT INTO blog_blog_upvotes(blog_id,user_id) VALUES(%s,%s) ', (post_id, user.id))
                conn.commit()
            updated = True
        '''for finding number of upvotes'''
        cur.execute('SELECT COUNT(*) FROM blog_blog_upvotes WHERE blog_id=' + str(post_id))
        upvotes_count = cur.fetchone()[0]
        data = {
            "updated": updated,
            "liked": liked,
            "upvotes": upvotes_count
        }
        return Response(data)


class InterestAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = interest.objects.all()
        if self.q:
            qs = qs.filter(interest_name__istartswith=self.q)
        # print(qs)
        return qs


class createView(APIView):

    def post(self, request):
        print(request.data)
        serializer = interestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #print(serializer.author.username)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BlogView(APIView):

    def get(self,request,interest_name):
        int1 = interest.objects.filter(interest_name=interest_name)
        if int1.exists():
            int1=interest.objects.get(interest_name=interest_name)

        int2 = Blog.objects.filter(interests=int1)
        if int2.exists():
            serializer = BlogSerializer(int2, many=True)
            return Response(serializer.data)
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)