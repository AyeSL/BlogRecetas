from django.urls import path
<<<<<<< HEAD
from AppBlog import views

urlpatterns = [
    path("", views.inicio,name="Bienvenidos"), 
    path("busquedaReceta/", views.buscarreceta),
=======
from .views import inicio

urlpatterns = [
    path("", inicio,name="inicio"), 
   # path("busquedaReceta/",buscarreceta), 
>>>>>>> e6590b78e1cc4fb9c83d1cf9f0e94562185b1363
   
]