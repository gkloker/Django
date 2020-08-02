# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from careers.models import Career

# Create your views here.
def careers(request):
    careers = Career.objects.all()

    return render(request, "careers.html", {"careers": careers})