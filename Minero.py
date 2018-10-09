import os
from pathlib import Path
import eyed3


class Minero():

    def __init__(self, path):
        self.lista_archivos = []
        self.lista_directorios = os.walk(path) 
        self.lista_artistas = []
        self.lista_canciones = []
        self.lista_albums = []

    def busca_mp3(self):
        for raiz, directorios, archivos in self.lista_directorios:
            for fichero in archivos:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".mp3"):
                    self.lista_archivos.append(nombreFichero + extension)
        return self.lista_archivos

    def tag_cancion(self,path):
        lista = self.busca_mp3()
        for i in lista:
            mp3 = eyed3.load(path + "/" + i)
            self.lista_canciones.append(mp3.tag.title)
        return self.lista_canciones

    def tag_artista(self,path):
        lista = self.busca_mp3()
        for i in lista:
            mp3 = eyed3.load(path + "/" + i)
            self.lista_artistas.append(mp3.tag.artist)
        return self.lista_artistas

    def tag_album(self,path):
        lista = self.busca_mp3()
        for i in lista:
            mp3 = eyed3.load(path + "/" + i)
            self.lista_albums.append(mp3.tag.album)
        return self.lista_albums

            
ruta = str(Path.home().resolve()) + "/Música"
s = Minero(ruta)
print(s.tag_cancion(ruta))
print(s.tag_artista(ruta))
print(s.tag_album(ruta))

