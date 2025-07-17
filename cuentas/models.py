from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    usuario     = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar      = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biografia   = models.TextField(blank=True)
    fecha_nac   = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

@receiver(post_save, sender=User)
def crear_actualizar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    instance.perfil.save()
