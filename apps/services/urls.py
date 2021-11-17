from django.urls import path, include
from .views import (
    ServicesCreate,
    ServicesList,
    ServicesDetail,
    ServicesEdit
)

urlpatterns = [
    path('create/<int:pk>', ServicesCreate.as_view(), name='services_create'),
    path('edit/<int:pk>', ServicesEdit.as_view(), name='services_edit'),
    path('list/', ServicesList.as_view(), name='services_list'),
    path('detail/<int:pk>', ServicesDetail.as_view(), name='services_detail'),
    path('summernote/', include('django_summernote.urls')),
    #path('perfil/', PerfilCreate.as_view(), name='perfil_edit'),
]
