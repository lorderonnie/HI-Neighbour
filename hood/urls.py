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
    path('add/business/',views.add_business,name = 'add_business'),
    path('neighbourhood/<int:id>',views.locationview, name="location"),
    path('hospital/<int:id>',views.hospitalview,name='hospital'),
    path('business/<int:id>',views.businessview,name = 'business'),
    path('police/<int:id>',views.policeview, name='police'),    
    
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






