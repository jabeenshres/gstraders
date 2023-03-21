from django import forms

from extras.models import HeroPage


class HeroPageForm(forms.ModelForm):
    class Meta:
        model = HeroPage
        fields = "__all__"
