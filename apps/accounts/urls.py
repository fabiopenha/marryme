from django.urls import path
from .views import UserCreate, PerfilCreate, PasswordsChangeView, SucessView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', UserCreate.as_view(), name='user_create'),
    path('perfil/', PerfilCreate.as_view(), name='perfil_edit'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordsChangeView.as_view(), name='password_change'),
    path('password-change/done', SucessView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete',),
]
