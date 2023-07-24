from django.db import models

# Create your models here.

 

class Artista(models.Model):
    nome = models.CharField('nome', max_length=30)
    #musicas = models.ManyToManyField(Musica, blank=True)


    def __str__(self):
        return self.nome
    
class Musica(models.Model):
    titulo = models.CharField('titulo', max_length=40)
    letra = models.TextField('letra', max_length=3000)
    artista = models.ForeignKey(Artista, blank=True, null=True, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.titulo
    #__str__.allow_tags = True