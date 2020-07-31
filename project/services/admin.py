# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Services

# Register your models here.

# agrega en el panel de admin el modelo servicios

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Services, ServicesAdmin)