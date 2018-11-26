# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=30)
    f_creacion = models.DateField()
class producto(models.Model):
    nombreProducto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField()
    n_existencias = models.IntegerField()
    categoria = models.ForeignKey('categoria',on_delete=models.CASCADE,)
