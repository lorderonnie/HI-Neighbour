from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse
from .models import Profile
from .forms import UpdateProfileForm,UserUpdateform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    current_user = request.user
    users = User.objects.all()
    
    return render(request,'head/home.html',{"current_user":current_user,"users":users})



def profile(request):
    name = request.user
    profile = Profile.get_profile_by_name(name)
    projects= Projects.get_project_by_name(name)

    return render(request,"profile/profile.html",{"profile":profile,"projects":projects,"name":name})


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



def logout(request):
    logout(request)
    
    return redirect('home')
