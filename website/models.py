from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.first_name
