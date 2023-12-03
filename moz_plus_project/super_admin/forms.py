from django import forms

from .models import (
    ContentRating,
    Country,
    Genre,
    Language,
    ShowRole,
    Studio,
    SubscriptionPlan,
)


class AddCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ("name",)


class EditCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ("name",)


class AddLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("name",)


class EditLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ("name",)


class AddContentRatingForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = (
            "name",
            "age",
        )


class EditContentRatingForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = (
            "name",
            "age",
        )


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("name",)


class EditGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ("name",)


class AddShowRoleForm(forms.ModelForm):
    class Meta:
        model = ShowRole
        fields = ("name",)


class EditShowRoleForm(forms.ModelForm):
    class Meta:
        model = ShowRole
        fields = ("name",)


class AddStudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = (
            "name",
            "image",
            "country",
        )


class EditStudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = (
            "name",
            "image",
            "country",
        )


class AddSubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = (
            "name",
            "cost",
            "months",
        )


class EditSubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = (
            "name",
            "cost",
            "months",
        )
