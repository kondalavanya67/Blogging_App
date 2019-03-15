from django.db import models
# Create your models here.
class Blog(models.Model):
    blog_id=models.CharField(max_length=1000000,unique=True)
    heading=models.CharField(max_length=100)
    content=models.CharField(max_length=1000000)
    post_date=models.DateTimeField(auto_now_add=True)
    upvotes=models.InigerField(default=0)
    def __str__(self):
        return self.Blog_id

class Comment(models.Model):
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    content=models.CharField(max_length=100)
    comment_date=models.DateTimeField(auto_now_add=True)
    upvotes=models.InigerField(default=0)

    def __str__(self):
        return self.Comment_id
