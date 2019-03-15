from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    heading=models.CharField(max_length=200)
    content=RichTextUploadingField()
    post_date=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    #post_category = models.ForeignKey()
    def __str__(self):
        return self.Blog_id
