from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistroForm, PerfilForm
from django.contrib.auth.models import User

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

class PerfilDetalle(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/perfil.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user

class PerfilEditar(LoginRequiredMixin, UpdateView):
    model       = User
    form_class  = PerfilForm
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user.perfil
