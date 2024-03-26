from django.conf import settings
from django.conf.urls.static import static
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
router.register(r'food', views.FoodViewSet)
router.register(r'ingredient', views.IngredientViewSet)
router.register(r'profile', views.ProfileViewSet)

urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
