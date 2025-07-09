from pygame import mixer as reproductor
iniciar = reproductor.init
cargar = reproductor.music.load
reproducir = reproductor.music.play
detener = reproductor.music.stop

iniciar()

print("Que canción quieres reproducir?")
cancion = input()
if cancion == 'perreito':
 cargar("./musica/Post Malone - Congratulations ft. Quavo.mp3")
elif cancion == 'tumbao':
    cargar("./musica/wwd.mp3juice.blog - Xavi - Flores (Official Video).mp3")

reproducir()

input("Presiona la tecla enter para detener la canción")

detener()
