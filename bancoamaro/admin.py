from django.contrib import admin

# Register your models here.

from .models import Cliente,Operacao2

admin.site.register(Cliente)
admin.site.register(Operacao2)