"""MisPerrisDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home,galeria,formulario,listar_personas,eliminar_personas,modificar_personas,agregarMascota,listarMascotas,eliminarMascota,modificarMascotas

urlpatterns = [
    path('', home, name='home'),
    path('galeria/',galeria,name='galeria'),
    path('formulario/',formulario,name="formulario"),
    path('listar_personas/',listar_personas,name="listar_personas"),
    path('eliminar_persona/<id>/',eliminar_personas,name="eliminar_persona"),
    path('modificar_personas/<id>/',modificar_personas,name="modificar_personas"),
    path('agregarMascota/',agregarMascota,name="agregarMascota"),
    path('listarMascotas/',listarMascotas,name="listarMascotas"),
    path('eliminarMascota/<id>/',eliminarMascota,name="eliminarMascota"),
    path('modificarMascota/<id>/',modificarMascotas,name="modificarMascotas"),
    #borre los import de los 2 path comentado ya que me tiraba error al momento de arrancar el server
]

