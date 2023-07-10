from django.db import models

# Create your models here.
class Stihovi(models.Model):

    naslov = models.CharField(max_length=120)
    objavljeno = models.CharField(max_length=200, blank=True)
    pesma = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.naslov
