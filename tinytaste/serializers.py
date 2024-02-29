from rest_framework import serializers

from tinytaste.models import Food


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['name']
