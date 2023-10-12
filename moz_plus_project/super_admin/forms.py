from django import forms

from .models import Country, Language


class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = 'name',


class EditCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = 'name',


class AddLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = 'name',
