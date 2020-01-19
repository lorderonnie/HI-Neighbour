from django.contrib import admin
from .models import Profile,Post,Health,Business,Police,Neighbourhood
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Health)
admin.site.register(Police)
admin.site.register(Neighbourhood)
