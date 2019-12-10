from django.db import models
import uuid as uuid_lib

from user.models import User


class TechnologyType(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TechnologyLevel(models.Model):
    level = models.IntegerField()
    text = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Technology(models.Model):
    technology_id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    user = models.ForeignKey(
        User,
        related_name='technologies',
        on_delete=models.CASCADE
    )
    technology_type = models.ForeignKey(
        TechnologyType,
        on_delete=models.CASCADE,
    )
    technology_level = models.ForeignKey(
        TechnologyLevel,
        on_delete=models.CASCADE,
    )
    years_of_experience = models.IntegerField(default=0)
    months_of_experience = models.IntegerField(default=0)
    not_want_to_use = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    product_id = models.UUIDField(
        primary_key=True,
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
    text = models.TextField(default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    experience_id = models.UUIDField(
        primary_key=True,
        editable=False
    )
    user = models.ForeignKey(
        User,
        related_name='Experiences',
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
    text = models.TextField(default='')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
