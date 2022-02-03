from django.contrib import admin
from .models import Client, Entity, Department
# Register your models here.

admin.site.register(Client)
admin.site.register(Entity)
admin.site.register(Department)
