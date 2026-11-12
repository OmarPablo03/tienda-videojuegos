from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    plataforma = models.CharField(max_length=50)
    genero = models.CharField(max_length=50, default="Acción")
    desarrolladora = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.plataforma})"