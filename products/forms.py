from django import forms


class ProductForm(forms.Form):
    sku = forms.CharField(max_length=50)
    quantity = forms.IntegerField()
