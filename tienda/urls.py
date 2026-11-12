from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaVideojuegos.as_view(), name='lista_videojuegos'),
    path('juego/<int:pk>/', views.DetalleVideojuego.as_view(), name='detalle_videojuego'),
    path('juego/nuevo/', views.CrearVideojuego.as_view(), name='crear_videojuego'),
    path('juego/<int:pk>/editar/', views.EditarVideojuego.as_view(), name='editar_videojuego'),
    path('juego/<int:pk>/borrar/', views.BorrarVideojuego.as_view(), name='borrar_videojuego'),
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('panel/', views.PanelInicio.as_view(), name='panel'),
]