import re
from django.core.exceptions import ValidationError

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

    def clean_background_color(self):
        hex_color_pattern = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
        background_color = self.cleaned_data.get('background_color')
        if not hex_color_pattern.match(background_color):
            raise ValidationError("Invalid hex color code.")
        return background_color


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = [
            "slug"
        ]
        fields = "__all__"