from django.contrib import admin

# Register your models here.

from .models import Querstion, Choice

admin.site.register(Querstion)
admin.site.register(Choice)
