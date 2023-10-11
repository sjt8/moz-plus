from django.shortcuts import render
from django.apps import apps


# Create your views here.
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
