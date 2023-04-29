from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    


    path("precios", views.precios, name="precios"),
    path("precios/add", views.add_precios, name="agregar_precios"),
    path("precios/edit/<str:pk>", views.edit_precios, name="editar_precios"),
    path("precios/delete/<str:pk>", views.delete_precios, name="eliminar_precios"),


    path("material", views.material, name="material"),
    path("material/add", views.add_material, name="agregar_material"),
    path("material/edit/<str:pk>", views.edit_material, name="editar_material"),
    path("material/delete/<str:pk>", views.delete_material, name="eliminar_material"),


    path("suplidor", views.suplidor, name="suplidor"),
    path("suplidor/add", views.add_suplidor, name="agregar_suplidor"),
    path("suplidor/edit/<str:pk>", views.edit_suplidor, name="editar_suplidor"),
    path("suplidor/delete/<str:pk>", views.delete_suplidor, name="eliminar_suplidor"),


    path("proyecto", views.proyecto, name="proyecto"),
    path("proyecto/add", views.add_proyecto, name="agregar_proyecto"),
    path("proyecto/edit/<str:pk>", views.edit_proyecto, name="editar_proyecto"),
    path("proyecto/delete/<str:pk>", views.delete_proyecto, name="eliminar_proyecto"),



    path("cliente", views.cliente, name="cliente"),
    path("add_cliente", views.add_cliente, name="add_cliente")
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)