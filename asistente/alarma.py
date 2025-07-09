
import time
import pygame

# Inicializar el reproductor de pygame
pygame.mixer.init()

def alarma(minutes, seconds):
    # Ruta del archivo de sonido
    sonido = r"./musica/Xavi.mp3"

    
    # Verificar que la ruta es correcta
    print(f"Ruta del archivo de sonido: {sonido}")
    
    # Convertir minutos y segundos a segundos totales
    total_seconds = minutes * 60 + seconds
    print(f'La alarma sonará en {minutes} minutos y {seconds} segundos...')
    
    # Esperar el tiempo especificado
    time.sleep(total_seconds)
    
    try:
        # Reproducir el sonido
        pygame.mixer.music.load(sonido)
        pygame.mixer.music.play()
        print("¡Es hora!")
        
        # Esperar hasta que se presione Enter para detener la alarma
        input("Presiona Enter para detener la alarma.")
        pygame.mixer.music.stop()
    except pygame.error:
        print(f"Error al intentar cargar el archivo de sonido en la ruta: {sonido}")

# Solicitar entrada al usuario
minutes = int(input("Ingresa los minutos de la alarma: "))
seconds = int(input("Ingresa los segundos de la alarma: "))

# Llamar a la función
alarma(minutes, seconds)
