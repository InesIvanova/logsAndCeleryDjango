from django.db import models


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_link_url = models.CharField(max_length=255)
