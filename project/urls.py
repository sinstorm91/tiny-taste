from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from tinytaste import views

urlpatterns = [
    path("tinytaste/", include("tinytaste.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router = routers.DefaultRouter()
router.register(r'foods', views.FoodViewSet)

urlpatterns += router.urls
