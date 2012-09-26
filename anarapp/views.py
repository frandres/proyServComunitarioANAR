#coding: latin-1

from anarapp.models import Yacimiento
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    lista_de_yacimientos = Yacimiento.objects.all().order_by('nombre')
    return render(request, 'yacimientos/index.html', {
        'yacimientos':lista_de_yacimientos
        })
