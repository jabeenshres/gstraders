from django import forms
from extras.models import HeroPage, Contact

class HeroPageForm(forms.ModelForm):
    class Meta:
        model = HeroPage
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
