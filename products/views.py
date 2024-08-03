from decimal import Decimal

from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin

from coupon_management_system.forms import CouponForm
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.decorators import action
from .forms import ProductForm


# Create your views here.
class ProductAPI(GenericViewSet, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        quantity_in_stock = request.data.get("quantity_in_stock")
        kwargs["partial"] = True
        if not quantity_in_stock:
            return Response("Please provide quantity in stock", status=HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data={"quantity_in_stock": quantity_in_stock}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=HTTP_200_OK)

    @action(methods=["POST", "GET"], detail=False, url_path="add")
    def add_product(self, request, *args, **kwargs):
        message = ""
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                sku = request.data["sku"]
                quantity = int(request.data.get("quantity", 1))
                product = self.get_queryset().filter(sku=sku).first()
                if product and product.quantity_in_stock >= quantity:
                    total_price = quantity * product.price
                    cart = request.session.pop('cart', {})
                    cart[product.name] = {"sku": product.sku, "quantity": quantity,
                                          "total_price": str(total_price)}
                    request.session["cart"] = cart
                    final_price = Decimal(0)
                    for item, value in cart.items():
                        final_price = final_price + Decimal(value["total_price"])
                    request.session["final_price"] = str(final_price)
                    message = "Product Added successfully"
                    form.clean()
                elif not product:
                    message = f"No Product Found with sku {sku}"
                else:
                    message = f"Quantity mentioned is greater than available.\n Available Quantity: {product.quantity_in_stock}"

        else:
            form = ProductForm()
        return render(request, 'product.html', context={"form": form, "message": message})

    @action(methods=["GET"], detail=False, url_path='cart')
    def cart(self, request, *args, **kwargs):
        cart = request.session.get("cart", {})
        final_price = request.session["final_price"]
        error = request.session.get("error", "")
        form = CouponForm()
        return render(request, 'cart.html', context={"cart": cart, "final_price": final_price,
                                                     "form": form, "error": error})
