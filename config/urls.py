from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tienda import views as tienda_views  # <-- Importamos las vistas de la tienda

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de autenticación por defecto (login/logout)
    path('accounts/', include('django.contrib.auth.urls')),
    # Ruta personalizada para el registro
    path('accounts/registro/', tienda_views.RegistroUsuario.as_view(), name='registro'),
    # Rutas de la tienda
    path('', include('tienda.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)