from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.first_name

@receiver(pre_delete, sender=Person)
def delete_img(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.img:
        instance.img.delete(False)
