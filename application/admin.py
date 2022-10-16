from django.contrib import admin
from .models import User, FoodMaker, FoodConsistence, AvailableWeight, FoodName
from django.contrib.auth.models import Permission, ContentType

admin.site.register(User)
admin.site.register(FoodMaker)
admin.site.register(FoodConsistence)
admin.site.register(AvailableWeight)
admin.site.register(FoodName)
admin.site.register(Permission)
admin.site.register(ContentType)
