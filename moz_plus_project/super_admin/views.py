from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.apps import apps

from . import forms


# Create your views here.
@login_required
def admin_super(request):
    menus = ['Country', 'Language']
    active = request.GET.get('active') or menus[0]
    values = apps.get_model('super_admin', active).objects.all()

    context = {
        'menus': menus,
        'active': active,
        'values': values
    }
    return render(request, 'super_admin/super_admin.html', context)


@login_required
def add_values(request, active, active_id):
    admin_forms = {
        'Country': forms.AddCountryForm,
        'Language': forms.AddLanguageForm,
    }
    values = apps.get_model('super_admin', active).objects.get(id=active_id)

    if request.method == 'POST':
        form = admin_forms.get(active)(request.POST, instance=values)
        if form.is_valid():
            form.save()
            return redirect('super_admin:super_admin',)

    else:
        form = admin_forms.get(active)()

    return render(request, 'super_admin/add_values.html', context={'form': form})
