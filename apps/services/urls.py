from django.urls import path, include
from .views import (
    ServicesCreate,
    ServicesList,
    ServicesListControl,
    ServiceSearch,
    ServicesDetail,
    ServicesEdit,
    ServiceDelete
)

urlpatterns = [
    path('create/<int:pk>', ServicesCreate.as_view(), name='services_create'),
    path('edit/<int:pk>', ServicesEdit.as_view(), name='services_edit'),
    path('list/', ServicesList.as_view(), name='services_list'),
    path('list/control', ServicesListControl.as_view(), name='services_list_control'),
    path('list/search', ServiceSearch.as_view(), name='services_search'),
    path('detail/<int:pk>', ServicesDetail.as_view(), name='services_detail'),
    path('delete/<int:pk>', ServiceDelete.as_view(), name='services_delete'),
    path('summernote/', include('django_summernote.urls')),
    #path('perfil/', PerfilCreate.as_view(), name='perfil_edit'),
]
