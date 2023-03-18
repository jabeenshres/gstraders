from django import forms

from products.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={'type': 'date'})
        }