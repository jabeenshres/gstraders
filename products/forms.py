from django import forms

from products.models import Products, Category

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = [
            "slug"
        ]
        # fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={'type': 'date'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = [
            "slug"
        ]
        fields = "__all__"