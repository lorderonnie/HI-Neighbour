from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import *
from .forms import UpdateProfileForm,UserUpdateform, NewPostForm,BusinessForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .email import send_welcome_email


# Create your views here.
@login_required(login_url = '/accounts/login/') 
def home(request):
    current_user = request.user
    posts= Post.get_all_posts()
    users = User.objects.all()
    return render(request,'head/home.html',{"users":users,"posts":posts})

@login_required(login_url = '/accounts/login/') 
def police(request):
    if request.method=='POST':
        form = NewPoliceForm(request.POST,request.FILES)
    if form.is_valid():
        police=form.save(commit=False)
        police.user = request.user
        current_user = request.user
        polices = Police.get_all_polices()
        police.save()

        return redirect('home')

    else:
        form = NewPoliceForm()
    
    return render(request,'head/police.html',{"form":form,"polices":polices})


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
        current_user = get_object_or_404(Profile,user = request.user)
        current_user = Profile.objects.get(user=request.user)
        business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
        police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
        hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
        user = request.user
        business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
        locations = Neighbourhood.objects.all()
        form = BusinessForm()
        context = {
            'business':business,
            'police':police,
            'hospitals':hospitals,
            'user':user,
            'current_user':current_user,
            'locations':locations,
            
        }
    return render(request,"profile/updateprofile.html",{"form":form,"form1":form1})

@login_required(login_url = '/accounts/login/')  
def add_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        hood = request.POST.get('Location')
        if form.is_valid():
            bussiness = form.save(commit=False)
            bussiness.neighbourhood = hood
            bussiness.posted_by = request.user
            bussiness.save()
            return redirect('home')
        else:
            messages.info(request,"all fields are required")
            return redirect('head/add_business.html')
    else:
        current_user = get_object_or_404(Profile,user = request.user)
        current_user = Profile.objects.get(user=request.user)
        business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
        police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
        hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
        user = request.user
        business = Business.objects.filter(neighbourhood=current_user.neighbourhood)
        locations = Neighbourhood.objects.all()
        form = BusinessForm()
        context = {
            'business':business,
            'police':police,
            'hospitals':hospitals,
            'user':user,
            'current_user':current_user,
            'locations':locations,
            'form':form,
            
        }
        return render(request,'head/add_business.html',context)
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


@login_required(login_url = '/accounts/login/') 
def locationview(request,id):
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    locations = Neighbourhood.objects.all()  
    location = get_object_or_404(Neighbourhood,id=id)
    occupants = Profile.objects.filter(neighbourhood = location.name)
    hospital_list= Health.objects.filter(neighbourhood = location.name)
    police_list = Police.objects.filter(neighbourhood = location.name)
    business_list = Business.objects.filter(neighbourhood = location.name)
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'location':location,
        'occupants':occupants,
        'hospital_list':hospital_list,
        'police_list':police_list,
        'business_list':business_list  
    }
    return render(request,'head/hood.html',context)

@login_required(login_url = '/accounts/login/') 
def hospitalview(request,id):
    Hospital = get_object_or_404(Health,id = id)
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    locations = Neighbourhood.objects.all()
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'Hospital':Hospital
        
    }
    return render(request,'head/hospital.html',context)

@login_required(login_url = '/accounts/login/') 
def businessview(request,id):
    bs = get_object_or_404(Business,id=id)
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    locations = Neighbourhood.objects.all()
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'bs':bs,
    }
    return render(request,'head/business.html',context)

@login_required(login_url = '/accounts/login/') 
def policeview(request,id):
    plc = get_object_or_404(Police,id=id)
    current_user = Profile.objects.get(user=request.user)
    business = Business.objects.filter(neighbourhood = current_user.neighbourhood)
    police = Police.objects.filter(neighbourhood = current_user.neighbourhood)
    hospitals = Health.objects.filter(neighbourhood = current_user.neighbourhood)
    user = request.user
    locations = Neighbourhood.objects.all()
    context = {
        'business':business,
        'police':police,
        'hospitals':hospitals,
        'user':user,
        'current_user':current_user,
        'locations':locations,
        'plc':plc,
    }
    return render(request,'head/police.html',context)

