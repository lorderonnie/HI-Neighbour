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
    





