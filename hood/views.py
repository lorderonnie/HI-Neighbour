from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile,Post
from .forms import UpdateProfileForm,UserUpdateform,NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .email import send_welcome_email


# Create your views here.

def home(request):
    current_user = request.user
    users = User.objects.all()
    posts = Post.get_all_posts()
    return render(request,'head/home.html',{"posts":posts,"current_user":current_user,"users":users})



@login_required(login_url = '/accounts/login/')  
def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)

    return render(request,"profile/profile.html",{"profile":profile,"name":name})

@login_required(login_url = '/accounts/login/')  
def updateprofile(request):
       
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        form1 = UserUpdateform(request.POST,instance=request.user)
        if form.is_valid() and form1.is_valid():
            form1.save() 
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        form1 = UserUpdateform(instance=request.user)
    return render(request,"profile/updateprofile.html",{"form":form,"form1":form1})

@login_required(login_url = '/accounts/login/')
def newpost(request):
    if request.method=='POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')

    else:
        form = NewPostForm()
        
    return render(request,'head/newpost.html',{'form':form})

@login_required(login_url = '/accounts/login/')  
def logout(request):
    logout(request)
    
    return redirect('home')
