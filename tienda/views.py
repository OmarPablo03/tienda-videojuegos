from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Videojuego
from .forms import VideojuegoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# LISTAR
class ListaVideojuegos(LoginRequiredMixin, ListView):
    model = Videojuego
    template_name = 'tienda/lista_videojuegos.html'
    context_object_name = 'videojuegos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('buscar')
        plataforma = self.request.GET.get('plataforma')
        
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        if plataforma:
            queryset = queryset.filter(plataforma__icontains=plataforma)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Para llenar el combo de plataformas con las que ya existen en la BD
        context['plataformas'] = Videojuego.objects.values_list('plataforma', flat=True).distinct()
        return context

# VER DETALLE
class DetalleVideojuego(LoginRequiredMixin, DetailView):
    model = Videojuego
    template_name = 'tienda/detalle_videojuego.html'

# CREAR
class CrearVideojuego(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'tienda/formulario_videojuego.html'
    success_url = reverse_lazy('lista_videojuegos')
    def test_func(self):
        return self.request.user.is_staff

# EDITAR
class EditarVideojuego(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    template_name = 'tienda/formulario_videojuego.html'
    success_url = reverse_lazy('lista_videojuegos')
    def test_func(self):
        return self.request.user.is_staff

# BORRAR
class BorrarVideojuego(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Videojuego
    template_name = 'tienda/confirmar_borrado.html'
    success_url = reverse_lazy('lista_videojuegos')
    def test_func(self):
        return self.request.user.is_staff
class CustomLogoutView(LogoutView):
    next_page = 'login'
class RegistroUsuario(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

from django.db.models import Sum

class PanelInicio(LoginRequiredMixin, TemplateView):
    template_name = 'tienda/panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_juegos'] = Videojuego.objects.count()
        context['total_stock'] = Videojuego.objects.aggregate(Sum('stock'))['stock__sum'] or 0
        context['juegos_bajo_stock'] = Videojuego.objects.filter(stock__lt=5).count()
        return context