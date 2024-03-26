import uuid

from django.contrib.auth.models import User
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)


class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)


class Profile(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    favorites = models.ManyToManyField(Food)
    allergies = models.ManyToManyField(Ingredient)
