from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User  # Import the User model

# Register the User model
admin.site.register(User)
