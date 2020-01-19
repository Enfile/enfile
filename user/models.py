from django.db import models
import uuid as uuid_lib


class Account(models.Model):
    account_id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    sub = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    profile_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    icon_path = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    sex = models.IntegerField(default=0)
    birth_day = models.DateField(blank=True, null=True)
    school_year = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=256, blank=True, null=True)
    profile = models.CharField(max_length=256, blank=True, null=True)
    using_os = models.CharField(max_length=256, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    contact = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
