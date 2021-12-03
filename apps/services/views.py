from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.services.models import Services
from django.db.models import Q


class ServicesCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Services
    fields = ['service_titulo','service_descricao', 'data_public','categoria', 'service_imagem', 'ativo']
    template_name = 'services/services_create.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.usuario_id = self.kwargs['pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ServicesList(ListView):
    model = Services
    template_name = 'services/services_list.html'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = Services.objects.filter(usuario=self.request.user.id, ativo=True).order_by('-id')
            return qs
        else:

            qs = Services.objects.filter(ativo=True).order_by('-id')
            return qs


class ServiceSearch(ListView):
    model = Services
    template_name = 'services/services_list.html'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('q')

        if self.request.user.is_authenticated:
            qs = Services.objects.filter(usuario=self.request.user.id, ativo=True).order_by('-id')
            qs = qs.filter(
                Q(service_titulo__icontains=termo) |
                Q(categoria__categoria__icontains=termo) |
                Q(service_descricao__icontains=termo)
            )
            return qs

        else:
            qs = Services.objects.filter(ativo=True).order_by('-id')
            qs = qs.filter(
                Q(service_titulo__icontains=termo) |
                Q(categoria__categoria__icontains=termo) |
                Q(service_descricao__icontains=termo)
            )
            return qs


class ServicesDetail(DetailView):
    model = Services

    def get_queryset(self):
        if self.request.user.is_authenticated:
            self.object_list = Services.objects.filter(usuario=self.request.user.id)
            return self.object_list
        else:
            self.object_list = Services.objects.all()
            return self.object_list


class ServicesEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Services
    fields = ['service_titulo', 'service_descricao', 'data_public','categoria', 'service_imagem', 'ativo']
    template_name = 'services/services_create.html'
    success_url = reverse_lazy('services_list_control')


class ServicesListControl(LoginRequiredMixin, ListView):
    model = Services
    template_name = 'services/services_list_control.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            self.object_list = Services.objects.filter(usuario=self.request.user.id).order_by('-id')
            return self.object_list
        else:
            self.object_list = Services.objects.filter(ativo=True).order_by('-id')
            return self.object_list


class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Services
    success_url = reverse_lazy('services_list_control')