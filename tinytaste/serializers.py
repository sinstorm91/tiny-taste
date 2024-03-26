from rest_framework import serializers

from tinytaste.models import Food, Ingredient, Profile


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'image_url', 'description', 'instructions', 'ingredients']


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'image_url', 'favorites', 'allergies']

