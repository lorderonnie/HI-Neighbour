from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    url(r'^newpost/',views.newpost,name='newpost'),
    path('hood/profile/',views.profile,name="profile"),
    url(r'^updateprofile/$',views.updateprofile,name='updateprofile'),
    path('logout/',views.logout,name = 'logout'),  
    url(r'^home/',views.home,name='newpost'),
    
    
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






