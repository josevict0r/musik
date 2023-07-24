from django.shortcuts import render
from .models import Artista, Musica

def letra(request, musica_id):
    musica = Musica.objects.get(pk=musica_id)
    return render(request, 'letra.html', {'musica': musica, 'artista': musica.artista})

def artistas(request):
    lista_artistas = Artista.objects.all()
    return render(request, 'artistas.html', {'artistas': lista_artistas})    
    
def musicas(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    musicas = artista.musica_set.all()
    return render(request, 'musicas.html', {'musicas': musicas, 'artista': artista})
#tem q fazer um for

def home(request):
    return render(request, 'home.html', {})
