from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def form_dom(request):
    caminho = os.path.join(settings.BASE_DIR, "DOM", "templates", "index.html")
    return HttpResponse(open(caminho, encoding="utf-8").read())


# Create your views here.
