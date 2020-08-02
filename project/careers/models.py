# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Career(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'career'
        verbose_name_plural = 'careers'

    def __str__(self):
        return self.title