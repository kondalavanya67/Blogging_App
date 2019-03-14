from django.db import models
# Create your models here.
class Blog(models.Model):
    blog_id=models.CharField(max_length=1000000,unique=True)
    heading=models.CharField(max_length=100)
    content=models.CharField(max_length=1000000)
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id
