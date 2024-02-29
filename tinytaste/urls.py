from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("random", views.random_food_old, name="random"),
    path("random", views.random_food, name="random")
]
