from django import forms
from .models import Cloth
# Register your models here.
class ClothForm(forms.ModelForm):
    class Meta:
        model=Cloth
        fields="__all__"