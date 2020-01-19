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
    path('add/business/',views.add_bussiness,name = 'add_business'),
    path('neighbourhood/<int:id>',views.location_view, name="location"),
    path('hospital/<int:id>',views.hospital_view,name='hospital'),
    path('business/<int:id>',views.business_view,name = 'business'),
    path('police/<int:id>',views.police_view, name='police'),    
    
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






