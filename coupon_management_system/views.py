from django.utils import timezone
from django.shortcuts import render, redirect
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.decorators import action
from .serializers import CouponSerializer
from .forms import CouponForm
from .models import Coupon
from decimal import Decimal


# Create your views here.
class CouponAPI(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    serializer_class = CouponSerializer

    def get_queryset(self):
        return Coupon.objects.all()

    @action(methods=['POST', 'GET'], detail=False, url_path='validate')
    def validate_coupon(self, request, *args, **kwargs):
        cart = request.session.get("cart", {})
        final_price = Decimal(request.session["final_price"])
        error = ""
        if request.method == "POST":
            form = CouponForm(request.POST)
            if form.is_valid():
                code = request.data["code"]
                coupon = self.get_queryset().filter(code=code).first()
                current_time = timezone.now()
                if coupon and coupon.valid_from <= current_time <= coupon.valid_to and coupon.active:
                    discount_price = final_price * Decimal((coupon.discount / 100))
                    final_price = final_price - discount_price
                    request.session["final_price"] = str(final_price)
                else:
                    error = "Coupon Not Valid."
                    request.session["error"] = error
            form.clean()
        return redirect(to='/products/cart/')
