from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Pagina(models.Model):
    titulo     = models.CharField(max_length=200)
    subtitulo  = models.CharField(max_length=200, blank=True)
    contenido  = RichTextField()
    imagen     = models.ImageField(upload_to='paginas/', blank=True, null=True)
    creado_en  = models.DateTimeField(default=timezone.now)
    autor      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
