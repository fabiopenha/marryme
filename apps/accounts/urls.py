from django.urls import path
from .views import UserCreate, PerfilCreate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create/', UserCreate.as_view(), name='user_create'),
    path('perfil/', PerfilCreate.as_view(), name='perfil_edit'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
