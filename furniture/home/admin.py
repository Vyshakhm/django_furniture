from django.contrib import admin
from.models import *
# Register your models here.
class catAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,catAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['p_name']
    prepopulated_fields = {'slug':('p_name',)}

admin.site.register(product,productAdmin)