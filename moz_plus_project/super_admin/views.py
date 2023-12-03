from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms


# Create your views here.
@login_required
def admin_super(request):
    menus = [
        "Country",
        "Language",
        "ContentRating",
        "Genre",
        "ShowRole",
        "Studio",
        "SubscriptionPlan",
    ]
    active = request.GET.get("active") or menus[0]
    values = apps.get_model("super_admin", active).objects.all()

    context = {
        "menus": menus,
        "active": active,
        "values": values,
    }
    return render(request, "super_admin/super_admin.html", context)


@login_required
def add_values(request, active):
    admin_forms = {
        "Country": forms.AddCountryForm,
        "Language": forms.AddLanguageForm,
        "ContentRating": forms.AddContentRatingForm,
        "Genre": forms.AddGenreForm,
        "ShowRole": forms.AddShowRoleForm,
        "Studio": forms.AddStudioForm,
        "SubscriptionPlan": forms.AddSubscriptionPlanForm,
    }

    if request.method == "POST":
        form = admin_forms.get(active)(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("super_admin:super_admin") + "?active=" + active,
            )

    else:
        form = admin_forms.get(active)()

    return render(
        request,
        "super_admin/add_values.html",
        context={
            "form": form,
            "active": active,
        },
    )


@login_required
def edit_values(request, active, active_id):
    admin_forms = {
        "Country": forms.EditCountryForm,
        "Language": forms.EditLanguageForm,
        "ContentRating": forms.EditContentRatingForm,
        "Genre": forms.EditGenreForm,
        "ShowRole": forms.EditShowRoleForm,
        "Studio": forms.EditStudioForm,
        "SubscriptionPlan": forms.EditSubscriptionPlanForm,
    }
    values = apps.get_model("super_admin", active).objects.get(id=active_id)

    if request.method == "POST":
        form = admin_forms.get(active)(request.POST, instance=values)
        if form.is_valid():
            form.save()
            return redirect(
                reverse("super_admin:super_admin") + "?active=" + active,
            )

    else:
        form = admin_forms.get(active)(instance=values)

    return render(
        request,
        "super_admin/edit_values.html",
        context={
            "form": form,
            "active": active,
        },
    )


@login_required
def delete_values(request, active, active_id):
    value = apps.get_model("super_admin", active).objects.get(id=active_id)
    value.delete()
    
    return redirect(
        reverse("super_admin:super_admin") + "?active=" + active,
    )
