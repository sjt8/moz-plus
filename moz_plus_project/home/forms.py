from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        max_length=20
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        max_length=20
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

    def check_confirm_password(self):
        cd = self.cleaned_data

        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Password not matching')

        return cd['confirm_password']


class CreatorRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        max_length=20
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        max_length=20
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

    def check_confirm_password(self):
        cd = self.cleaned_data

        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Password not matching')

        return cd['confirm_password']
