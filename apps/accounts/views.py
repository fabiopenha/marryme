from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Usuario

# Create your views here.


class UserCreate(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('home')


class PerfilCreate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'accounts/perfil.html'
    model = Usuario
    fields = ['empresa', 'telefone', 'categoria']
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Usuario, usuario=self.request.user)
        return self.object