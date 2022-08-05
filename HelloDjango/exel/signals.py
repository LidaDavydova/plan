from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from .models import *

@receiver(pre_delete, sender=Brief_pattern)
def file_delete(sender, instance, **kwargs):
    if instance.file.name:
        instance.file.delete(True)