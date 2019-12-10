from django.contrib import admin

from .models import Profile, User

@admin.register(Profile)
class Profile(admin.ModelAdmin):
  pass

@admin.register(User)
class User(admin.ModelAdmin):
  pass

