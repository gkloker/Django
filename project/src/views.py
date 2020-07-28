# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, "home.html")


def services(request):

    return render(request, "services.html")


def store(request):

    return render(request, "store.html")


def blog(request):

    return render(request, "blog.html")


def contact(request):

    return render(request, "contact.html")