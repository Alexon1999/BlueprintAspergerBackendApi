from django.contrib import admin
from .models import Utilisateur, Message
# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Message)
