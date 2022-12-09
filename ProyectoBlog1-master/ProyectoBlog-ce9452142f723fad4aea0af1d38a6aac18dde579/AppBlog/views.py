from django.shortcuts import render
from django.http import HttpResponse

from AppBlog.models import *
from django.core import serializers

from AppBlog.forms  import *

def inicio(request):
    return render(request,"AppBlog/inicio.html")

def buscarreceta(request):
    return render(request,"AppBlog/busquedaReceta.html")

def buscar(request):
   if request.GET["ingrediente"]:
    ingrediente = request.GET["ingrediente"]
    categoria =  categoria.objects.filter(ingrediente=ingrediente)
    return render(request,"AppBlog/busquedaReceta.html",{"ingrediente":ingrediente,"categoria":categoria})

def categoria(request):
    return render(request,"l")

def Blog(request):
    return HttpResponse ("Vista de Blog")

def Receta(request):
    if request.method == "POST":
            miFormulario = RecetaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  
                  busqueda_receta = categoria(ingrediente=informacion["ingrediente"], categoria=informacion["categoria"],)
                  busqueda_receta.save()
                  return render(request, "AppBlog/inicio.html")
    else:
        miFormulario = RecetaFormulario()
 
        return render(request, "AppBlog/RecetaFormulario.html", {"miFormulario": miFormulario})


def ingredientesapi(request):
    ingredientes_todos = categoria.objects.all()
    return HttpResponse(serializers.serialize('json',ingredientes_todos))
