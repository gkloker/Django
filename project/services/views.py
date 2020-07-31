# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from services.models import Services

# Create your views here.
def services(request):
    services = Services.objects.all()

    return render(request, "services.html", {"services": services})