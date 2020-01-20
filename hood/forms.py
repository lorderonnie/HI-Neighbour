from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from .models import Profile,Post,Business,Police
class Loginform(forms.Form):
    username =forms.CharField(label='Your username',max_length= 50)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user= User.objects.filter(username=username)
            if not user:
                raise forms.ValidationError('papapapapapa')
            if not user.check_password(password):
                raise forms.ValidationError('Incoreect password')
        return super(Loginform, self).clean(*args, **kwargs)
      
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user',
                   'neighbourhood',
]
class NewPoliceForm(forms.ModelForm):
    class Meta:
        model = Police
        exclude = ['user',
                   'neighbourhood',
]
       
class UpdateProfileForm(forms.ModelForm):
    bio = forms.Textarea()
    class Meta:
        model = Profile
        exclude =[
            'user',

]
class UserUpdateform(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = [
        'username',
        'email',
]       

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = [
            'neighbourhood',
            'posted_by'
        ]

      