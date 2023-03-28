from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("analisis", views.analisis, name="analisis"),
    path("precios", views.precios, name="precios"),
    path("material", views.material, name="material"),
    path("add_material", views.add_material, name="add_material")
]