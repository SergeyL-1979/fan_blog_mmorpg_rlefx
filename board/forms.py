from django import forms
from .models import Advertisement, Response


class RegistrationForm(forms.Form):
    # Добавьте поля для регистрации
    pass


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'text', 'category']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
