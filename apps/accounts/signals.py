from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from apps.accounts.models import Usuario


@receiver(post_save,sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario = instance)
    else:
        if not hasattr(instance,"usuario"):
            Usuario.objects.create(usuario=instance)
    instance.usuario.save()