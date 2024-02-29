from random import choice

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tinytaste.models import Food
from tinytaste.serializers import FoodSerializer


def index(request):
    return HttpResponse("Love you Danning &#x1F60D Welcome to the Tiny Taste.")


def random_food_old(request):
    baby_foods = [
        "Pureed carrots",
        "Mashed bananas",
        "Pureed sweet potatoes",
        "Avocado puree",
        "Pureed peas",
        "Applesauce",
        "Pureed butternut squash",
        "Oatmeal cereal (mixed with breast milk or formula)",
        "Pureed pears",
        "Plain yogurt (if recommended by pediatrician and if baby has started dairy)"
    ]
    return HttpResponse(choice(baby_foods))


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@api_view(['GET'])
def random_food(request):
    if request.method == 'GET':
        food = Food.objects.order_by('?')[0]
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)
    return Response({"message": "Only GET allowed"})
