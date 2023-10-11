from django.urls import path

from . import views

app_name = 'super_admin'

urlpatterns = [
    path('super/admin/', views.admin_super, name='super_admin')
]
