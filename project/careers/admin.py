# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Career

# Register your models here.
class CareersAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Career, CareersAdmin)