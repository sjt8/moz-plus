from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.password_validation import (
    validate_password,
    MinimumLengthValidator,
    NumericPasswordValidator,
)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data.get("username")
        user = User.objects.filter(username=data)

        if not user:
            raise forms.ValidationError("Username not found.")

        return data

    def clean(self):
        data = super().clean()
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username).first()

        if user and not user.check_password(password):
            raise forms.ValidationError("Username or Password not match.")

        return data


class UserRegistrationForm(forms.ModelForm):
    username_validator = ASCIIUsernameValidator()

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput,
        max_length=20,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        max_length=20,
    )

    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, max_length=20
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        min_length_validator = MinimumLengthValidator()
        password_validator = NumericPasswordValidator()

        validate_password(
            password, password_validators=[min_length_validator, password_validator]
        )
        raise password

    def clean_confirm_password(self):
        cd = self.cleaned_data

        if cd.get("password", "") != cd["confirm_password"]:
            raise forms.ValidationError("Password not matching")

        return cd["confirm_password"]


class CreatorRegistrationForm(forms.ModelForm):

    username_validator = ASCIIUsernameValidator()

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput,
        max_length=20,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
    )

    password = forms.CharField(
        label="Password", widget=forms.PasswordInput, max_length=20
    )
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, max_length=20
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        min_length_validator = MinimumLengthValidator()
        password_validator = NumericPasswordValidator()

        validate_password(
            password, password_validators=[min_length_validator, password_validator]
        )
        raise password

    def clean_confirm_password(self):
        cd = self.cleaned_data

        if cd.get("password", "") != cd["confirm_password"]:
            raise forms.ValidationError("Password not matching")

        return cd["confirm_password"]
