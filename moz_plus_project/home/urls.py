from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('register/', views.subscriber_registration, name='register'),
    path('content-creator/register/', views.creator_registration,
         name='register_creator'),
]
