from django.urls import path
from .views import ProductAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductAPI, basename='ProductAPI')

urlpatterns = [
] + router.urls
