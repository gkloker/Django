# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("home")


def services(request):
    return HttpResponse("services")


def store(request):
    return HttpResponse("store")


def blog(request):
    return HttpResponse("blog")


def contact(request):
    return HttpResponse("contact")