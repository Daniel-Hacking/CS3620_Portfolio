from django.contrib import admin
from .models import Portfolio_item, Hobby, Contact_Info

# Register your models here.

admin.site.register(Portfolio_item)
admin.site.register(Hobby)
admin.site.register(Contact_Info)

