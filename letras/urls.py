from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('musicas/<artista_id>', views.musicas, name="musicas"),
    path('', views.artistas, name="artistas"),
    path('letra/<musica_id>', views.letra, name="letra"),
]