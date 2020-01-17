from django.shortcuts import get_object_or_404, redirect ,render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'head/home.html')

