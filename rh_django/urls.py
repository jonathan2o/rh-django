from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [

    path("admin/",admin.site.urls),
    #incluimos las rutas de la app empleados en la raiz
    path("",include("empleados.urls")),
]
