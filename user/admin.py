from django.contrib import admin

from .models import Account, Profile, User


@admin.register(Account)
class Account(admin.ModelAdmin):
    pass


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    pass


@admin.register(User)
class User(admin.ModelAdmin):
    pass

