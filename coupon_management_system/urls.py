
from rest_framework.routers import DefaultRouter
from .views import CouponAPI

router = DefaultRouter()
router.register('', CouponAPI, basename='CouponAPI')

urlpatterns = [
] + router.urls
