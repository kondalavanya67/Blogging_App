from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class interest(models.Model):
    interest_name=models.CharField(max_length=200)
    content=RichTextUploadingField()

class Blog(models.Model):
    author= models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    heading=models.CharField(max_length=200)
    content=RichTextUploadingField()
    post_date=models.DateTimeField(auto_now_add=True)
    upvotes=models.IntegerField(default=0)
    interests=models.ManyToManyField(interest,null=True,blank=True)
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author= models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    comment_date=models.DateTimeField(auto_now_add=True)
    upvotes=models.IntegerField(default=0)


    def __str__(self):

       return str(self.id)
