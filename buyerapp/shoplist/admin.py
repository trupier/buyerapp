from django.contrib import admin

# Register your models here.
from .models import Shoplist, Item

admin.site.register(Shoplist)
admin.site.register(Item)