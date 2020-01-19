from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete = models.CASCADE, default='')
    profile_pic = models.ImageField(upload_to = 'media/', default='default.jpg')
    bio =models.TextField()
    neighbourhood = models.CharField(max_length=60)
    updated_on = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return user
    
    def save_profile(self):
        
        self.save()
    @classmethod
    def get_profile_by_name(cls,name):
       
        profile = cls.objects.filter(user = name)

        return  name 
    

class Post(models.Model):
    picture = models.ImageField(upload_to= 'media/')
    caption= models.CharField(max_length=50)
    details = models.TextField(blank=True)
    neighbourhood = models.CharField(max_length=60)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    

    @classmethod
    def get_all_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def get_post_by_name(cls,name):
        posts = cls.objects.filter(name= name)
        return posts  
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


