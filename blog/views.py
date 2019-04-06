from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import story, comment
from .models import Blog, Comment, interest
from dal import autocomplete
from django.views.generic import RedirectView
from rest_framework import status

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
from blog.serializer import BlogSerializer
from blog.serializer import interestSerializer

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

class interestView(APIView):
    def get(self,request):
        int1 = interest.objects.all()
        serializer = interestSerializer(int1, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = interestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class BlogView(APIView):
    def get(self,request):
        int1 = Blog.objects.all()
        serializer = BlogSerializer(int1, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
