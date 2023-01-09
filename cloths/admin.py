from django.contrib import admin
from .models import Cloth

class ClothAdmin(admin.ModelAdmin):
    list_display = ['colour','size','dop','email','quantity','gender']

admin.site.register(Cloth,ClothAdmin)