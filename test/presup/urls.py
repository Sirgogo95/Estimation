from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("analisis", views.analisis, name="analisis"),
    path("precios", views.precios, name="precios"),
    path("add_precios", views.add_precios, name="add_precios"),
    path("eliminar_precios", views.eliminar_precios, name="eliminar_precios"),
    path("material", views.material, name="material"),
    path("add_material", views.add_material, name="add_material"),
    path("eliminar_material", views.eliminar_material, name="eliminar_material"),
    path("suplidor", views.suplidor, name="suplidor"),
    path("add_suplidor", views.add_suplidor, name="add_suplidor"),
    path("eliminar_suplidor", views.eliminar_suplidor, name="eliminar_suplidor")
]
