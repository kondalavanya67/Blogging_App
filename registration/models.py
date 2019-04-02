import os
import random
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from blog.models import interest, Blog
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('others','OTHERS'),
)

def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name,ext=os.path.splitext(base_name)
	return name,ext

def upload_image_path(instance, filename):
	new_filename=random.randint(1,50000)
	name,ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "user/{new_filename}/{final_filename}".format(
		             new_filename=new_filename,final_filename=final_filename)


	
class profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	fullname=models.CharField(max_length=120)
	age=models.IntegerField( default=25,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
	gender=models.CharField(max_length=10,choices=GENDER_CHOICES, default='male')
	phone_no=models.CharField(max_length=11)
	image=models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	active=models.BooleanField(default=False)
	interest=models.ManyToManyField(interest, blank=True)
	post=models.ManyToManyField(Blog, blank=True)

	

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return "/user/{id}/".format(id=self.id)

	def get_absolute_url_profile(self):
		return reverse('registration:show_profile',kwargs={'pk':self.pk})
        

class Follower(models.Model):
    follower = models.ForeignKey(profile, related_name='following',on_delete=models.CASCADE)
    following = models.ForeignKey(profile, related_name='followers',on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)
    



# Create your models here.


# Create your models here.