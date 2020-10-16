from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from .models import Person

@receiver(post_delete, sender=Person)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.img.delete(save=False)
