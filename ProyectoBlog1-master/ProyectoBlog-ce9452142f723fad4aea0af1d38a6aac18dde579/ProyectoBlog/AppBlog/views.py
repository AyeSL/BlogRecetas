from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
from AppBlog.models import post
=======
from AppBlog.models import categoria
from django.core import serializers

from AppBlog.forms  import RecetaFormulario

def inicio(request):
    return render(request,"AppBlog/inicio.html")

def buscarreceta(request):
    return render(request,"AppBlog/busquedaReceta.html")
  
def categoria(request):
    return render(request,"l")
>>>>>>> e6590b78e1cc4fb9c83d1cf9f0e94562185b1363

from AppBlog.forms  import RecetaFormulario

def inicio(request):
    return render(request,"AppBlog/inicio.html")

def buscarreceta(request):
    return render(request,"AppBlog/busquedaReceta.html")
  
def Blog(request):
    return HttpResponse ("Vista de Blog")

def categoria(request):
    if request.method == "POST":
            miFormulario = RecetaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  
                  busqueda_ingrediente = categoria(ingrediente=informacion["ingrediente"], categoria=informacion["categoria"])
                  busqueda_ingrediente.save()
                  return render(request, "AppBlog/inicio.html")
    else:
        miFormulario = RecetaFormulario()
 
    return render(request, "AppBlog/categoria.html", {"miFormulario": miFormulario})


def ingredientesapi(request):
    ingredientes_todos = categoria.objects.all()
    return HttpResponse(serializers.serialize('json',ingredientes_todos))
