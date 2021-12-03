from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import Usuario

# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_success')


class SucessView(TemplateView):
    template_name = 'registration/password_change_done.html'


class UserCreate(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        self.object = self.get_form()
        form = self.object

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            user.refresh_from_db()
            user.usuario.empresa = form.cleaned_data.get('empresa')
            user.usuario.telefone = form.cleaned_data.get('telefone')
            user.usuario.categoria = form.cleaned_data.get('categoria')
            user.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PerfilCreate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ('empresa','telefone', 'categoria',)
    template_name = 'accounts/perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Usuario, usuario=self.request.user)
        return self.object



