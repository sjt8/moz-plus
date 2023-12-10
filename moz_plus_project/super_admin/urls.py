from django.urls import path

from . import views

app_name = "super_admin"

urlpatterns = [
    path("super/admin/", views.admin_super, name="super_admin"),
    path("super/admin/value/add/<str:active>", views.add_values, name="add_values"),
    path(
        "super/admin/value/edit/<str:active>/<int:active_id>",
        views.edit_values,
        name="edit_values",
    ),
    path(
        "super/admin/value/delete/<str:active>/<int:active_id>",
        views.delete_values,
        name="delete_values",
    ),
]
