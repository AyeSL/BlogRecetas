from django.shortcuts import render
from django.http import HttpResponse

from AppBlog.models import post

from AppBlog.forms  import RecetaFormulario

def inicio(request):
    return render(request,"AppBlog/inicio.html")

def buscarreceta(request):
    return render(request,"AppBlog/busquedaReceta.html")
  
def Blog(request):

  return HttpResponse ("Vista de Blog")
