from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Ciius(models.Model):
    codigo = models.CharField(max_length=8)
    actividad = models.CharField(max_length=255)
    # Cuando hallan cambios en la base de datos se debe poner este código de abajo
    # class Meta:
    #     managed = False
    #     db_table = 'ciius'

    # def __str__(self):
    #     return self.codigo + ' ' + self.actividad

