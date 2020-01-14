from django.db import models
import uuid as uuid_lib

from user.models import User


class TechnologyLevel(models.Model):
    level = models.IntegerField(unique=True)
    text = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Technology(models.Model):
    technology_id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        User,
        related_name='technologies',
        on_delete=models.CASCADE
    )
    technology_level = models.ForeignKey(
        TechnologyLevel,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=256)
    years_of_experience = models.IntegerField(default=0)
    months_of_experience = models.IntegerField(default=0)
    not_want_to_use = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product_id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        User,
        related_name='products',
        on_delete=models.CASCADE
    )
    product_type = models.CharField(
        max_length=256,
        default='',
        blank=True
    )
    link = models.CharField(
        max_length=256,
        default='',
        blank=True
    )
    technology = models.CharField(
        max_length=256,
        default='',
        blank=True
    )
    text = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    experience_id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        User,
        related_name='experiences',
        on_delete=models.CASCADE
    )
    experience_type = models.CharField(
        max_length=256,
        default='',
        blank=True
    )
    link = models.CharField(
        max_length=256,
        default='',
        blank=True
    )
    technology = models.CharField(
        max_length=256,
        default='',
        blank=True
    )
    text = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
