# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # especificamos el nombre que va a tener el servicio en la base de datos
    class Meta:
        verbose_name = 'services'
        verbose_name_plural = 'services'

    # devuelve el titulo del servicio
    def __str__(self):

        return self.title