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

class Health(models.Model):
    neighbourhood = models.CharField(max_length=250)
    email =  models.EmailField()
    phone = models.IntegerField()
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'post/',blank=True)
    
    def __str__(self):
        return self.name

class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'post/',blank=True)
    
    def __str__(self):
        return self.name
 
class Police(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    neighbourhood = models.CharField(max_length=250)
    image =  models.ImageField(upload_to= 'post/', default= 'default.jpg')
    
    def __str__(self):
        return self.name
    
    
    
    
class Business(models.Model):
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE)
    neighbourhood = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image =  models.ImageField(upload_to= 'post/', default= 'default.jpg')
    
    def __str__(self):
        return self.name
