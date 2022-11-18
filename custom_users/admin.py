from django.contrib import admin

# Register your models here.
from custom_users.models import CustomUser

admin.site.register(CustomUser,)
