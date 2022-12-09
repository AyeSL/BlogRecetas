from django.urls import path
from .views import inicio
from AppBlog import views
urlpatterns = [
    path("", inicio,name="inicio"), 
    path("Receta/", views.Receta, name="categoria"),
    path("Blog/", views.Blog, name="Blog")
   # path("busquedaReceta/",buscarreceta), 
    
]