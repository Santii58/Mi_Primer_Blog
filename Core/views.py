from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Pagina
from .forms import PaginaForm

def inicio(request):
    return render(request, 'core/inicio.html')

@login_required
def acerca(request):
    return render(request, 'core/acerca.html')

class ListaPaginas(ListView):
    model = Pagina
    template_name = 'core/lista_paginas.html'
    context_object_name = 'paginas'

class DetallePagina(DetailView):
    model = Pagina
    template_name = 'core/detalle_pagina.html'
    context_object_name = 'pagina'

class CrearPagina(LoginRequiredMixin, CreateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'core/formulario_pagina.html'
    success_url = reverse_lazy('lista_paginas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPagina(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pagina
    form_class = PaginaForm
    template_name = 'core/formulario_pagina.html'
    success_url = reverse_lazy('lista_paginas')

    def test_func(self):
        return self.get_object().autor == self.request.user

class EliminarPagina(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pagina
    template_name = 'core/confirmar_borrado.html'
    success_url = reverse_lazy('lista_paginas')

    def test_func(self):
        return self.get_object().autor == self.request.user
