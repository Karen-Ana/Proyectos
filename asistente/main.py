##librerias
from speech_recognition import Recognizer, Microphone, UnknownValueError
from pyttsx3 import init as inicio
from pyperclip import copy as portapapeles
from wikipedia import set_lang as idioma, page as buscar
from os import makedirs, path, system as abrir
from subprocess import run as ejecutar
from pywhatkit import sendwhatmsg as enviar
from datetime import datetime as tiempo
from datetime import datetime as hora
from pygame import mixer as reproductor  # Ya estás importando mixer, no necesitas más
from requests import get as solicitud_get
from platform import system as sistema, node as nodo, version as version_so
from platform import machine as arquitectura, processor as procesador
from os import system as apa
from bs4 import BeautifulSoup
from time import sleep  # Importas solo la función sleep




iniciar = reproductor.init
cargar = reproductor.music.load
reproducir = reproductor.music.play
detener = reproductor.music.stop

z = inicio() #inicializar libreria
propiedad = z.setProperty
e = z.say
j = z.runAndWait
a= Recognizer()
pausas = a.pause_threshold=.8 # segundos de espera del microfono
p = a.listen
l = a.recognize_google

# Inicializar el reproductor de pygame
reproductor.init()


voz = r"HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_ES-ES_HELENA_11.0" #ruta de direccion de voz almacenada en el equipo

##funciones



def escuchar(mensaje=None):
    if mensaje:
        hablar(mensaje)  # Llama a la función hablar para pronunciar el mensaje
    with Microphone() as microfono:
        pausas
        print("Escuchando...")

        xvoz = p(microfono)  # Escuchando

        try:
            pedido = l(xvoz, language="es-mx")  # Transformar en texto el ruido
            print("Tú: " + pedido)
            return pedido  # Regresa la variable pedido
        except UnknownValueError:
            error = print("No te entendí...")
            return error
        except:  # Error de conexión
            conexion = print("Revisa tu conexión a internet...")
            return conexion


def hablar(mensaje):#funcion hablar declarar variable
    propiedad('voice', voz)#propiedad de voice a voz
    e(mensaje)#decir el mensaje
    j()#esperar a que hable y no dejar hacer otro comando
    
def dictado():
    hablar("¿Que quieres guardar en el portapapeles?")
    contenido = escuchar()
    portapapeles(contenido)
    hablar("La información se guardo satisfactoriamente en el portapapeles")

def tarea():
    idioma("es")

    hablar("Que tema quieres buscar....")
    clave = escuchar()
    respuesta = buscar(clave)

    hablar(f"Titulo: {respuesta.title}")
    hablar(f"Contenido: {respuesta.summary}")

def informacion():
    idioma("es")
    hablar("Qiue tema deseas buscar?")
    clave = escuchar()
    respuesta = buscar(clave)
    portapapeles("Titulo: "+respuesta.title+"\n Contenido: "+respuesta.summary)
    hablar("Se copio correctamente")

def estructura():
    ruta = r"C:\laragon\www"
    hablar("Como se va a llamar?")
    nom_pro = escuchar()
    ruta_nueva = path.join(ruta, nom_pro)

    try:
        makedirs(ruta_nueva)
        subrutas = ['assets','include','components','pages']
        for carp in subrutas:
            makedirs(path.join(ruta_nueva, carp))

        assets = ['css','js','media']
        for carp in assets:
            makedirs(path.join(ruta_nueva, 'assets', carp))

        indexr = path.join(ruta_nueva, 'index.html')
        with open(indexr, 'w') as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n   <title>Index</title>\n</head>\n<body>\n <h1>Bienvenidos</h1>\n</body>\n</html>")
        f.close

        hablar("Carpetas creadas")
    except FileExistsError:
        hablar("La carpeta ya existe")
    except Exception:
        hablar("Error al crear la carpeta")
def spotify():
    abrir("Spotify")
def app():
    ejecutar(["C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"])
def web():
    ejecutar(["C:/Program Files/Google/Chrome/Application/chrome.exe"]) 
def grafica():
    ejecutar(["C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"])    

def mensaje():
    # Pedir datos al usuario
    hablar("¿A qué número quieres mandar mensaje? (10 dígitos)")
    numero = escuchar()

    hablar("¿Qué mensaje quieres enviar?")
    mensaje = escuchar()

    # Obtener hora actual
    ahora = tiempo.now()
    ho = ahora.hour  # Hora actual
    mi = ahora.minute + 1  # Minuto actual + 1 (para programar el envío)

    # Concatenar el código de país
    numero_con_codigo = str("+52") + numero

    # Enviar mensaje
    enviar(numero_con_codigo, mensaje, ho, mi)  # número, mensaje, hora, minuto

def cancion():
    iniciar()

    hablar("Que canción quieres reproducir?")
    cancion = escuchar()
    
    if cancion == 'feliz':
        cargar("./musica/Congratulations.mp3")
    elif cancion == 'flores':
        cargar("./musica/Xavi.mp3")

    reproducir()
    hablar("Presiona la tecla enter para detener la canción")
    input()

    detener()

def fecha():
    fecha = hora.now()

    hablar("Hoy es el dia {} del año {} ".format(fecha.day, fecha.year))

def obtener_hora():
    hor = hora.now()
    periodo = ""

    # Determinar el periodo del día
    if 5 <= hor.hour < 12:
        periodo = "de la mañana"
    elif 12 <= hor.hour < 18:
        periodo = "de la tarde"
    else:
        periodo = "de la noche"

    hablar("La hora es {}:{:02d}, {}.".format(hor.hour, hor.minute, periodo))


def f_tempe():
        hablar("¿De qué ciudad quieres conocer el clima?")
        ciudad = escuchar()
        url_temp = f"https://wttr.in/{ciudad}?format=%t"
        url_clima = f"https://wttr.in/{ciudad}?format=%C"

        response_temp = solicitud_get(url_temp)  # Obtener la temperatura
        response_clima = solicitud_get(url_clima)  # Obtener la descripción del clima

        if response_temp and response_clima:
            # Verificar si la respuesta contiene "°C"
            if "°C" in response_temp.text:
                temp_celsius = float(response_temp.text.strip().replace("°C", ""))
                descripcion_clima = response_clima.text.strip()
                hablar(f"Estamos a {temp_celsius}°C en {ciudad}, y el clima está {descripcion_clima.lower()}.")
            else:
                hablar("No se pudo obtener la temperatura. Verifica la ciudad o el servicio.")
        else:
            hablar("Hubo un problema al obtener la información del clima.")



def info_pc():
    operating_system = sistema()
    node_name = nodo()
    operating_system_version = version_so()
    processor_architecture = arquitectura()
    processor_details = procesador()

    hablar(f"Sistema Operativo: {operating_system}")
    hablar(f"Nombre del Nodo: {node_name}")
    hablar(f"Versión del sistema operativo: {operating_system_version}")
    hablar(f"Arquitectura del Procesador: {processor_architecture}")
    hablar(f"Detalle del procesador: {processor_details}")       
def off():
    shutdown = escuchar('¿Quieres apagar el ordenador? (si/no)')

    if shutdown.lower() == 'si':
        os.system('shutdown /s /t 1')
    else:
        hablar("Cancelando el apagado.")

def obtener_noticias():
    url = "https://elpais.com/"
    
    # Realizar la solicitud a la página web
    respuesta = solicitud_get(url)
    
    if respuesta.status_code == 200:
        # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(respuesta.text, "html.parser")
        
        # Buscar titulares (en este caso, están en etiquetas <h2>)
        titulares = soup.find_all("h2", class_="c_t")
        
        if titulares:
            hablar("Noticias principales de El País:")
            for i, titular in enumerate(titulares[:10], 1):  # Obtener los primeros 10 titulares
                hablar(f"{i}. {titular.get_text(strip=True)}")
        else:
            hablar("No se encontraron titulares.")
    else:
        hablar(f"Error al acceder a la página: {respuesta.status_code}")

def poner_alarma():
    # Obtener la hora actual
    hora_actual = tiempo.now()  # Usar 'tiempo' en lugar de 'cita'
    hora_actual_str = hora_actual.strftime("%H:%M")
    print(f"Hora actual: {hora_actual_str}")
    
    # Pedir al usuario la hora en formato de 24 horas y los minutos
    hablar("¿A qué hora quieres que suene la alarma? Por favor, dime la hora en formato de 24 horas (ejemplo: 15 para las 3 PM).")
    hora_alarma = int(escuchar())  # Obtener la hora
    hablar("¿Y los minutos?")
    minutos_alarma = int(escuchar())  # Obtener los minutos
    
    # Crear un objeto de tiempo para la hora de la alarma
    alarma_time = hora_actual.replace(hour=hora_alarma, minute=minutos_alarma, second=0, microsecond=0)
    
    # Si la hora de la alarma ya pasó, programarla para el día siguiente
    if alarma_time < hora_actual:
        alarma_time = alarma_time.replace(day=hora_actual.day + 1)
    
    # Calcular la diferencia de tiempo hasta la alarma
    tiempo_restante = alarma_time - hora_actual
    total_seconds = tiempo_restante.total_seconds()
    
    # Ruta del archivo de sonido
    sonido = r"./musica/alarma.mp3"
    
    # Verificar que la ruta es correcta
    print(f"Ruta del archivo de sonido: {sonido}")
    
    # Anunciar cuánto tiempo queda para la alarma
    hablar(f'La alarma sonará en {tiempo_restante.seconds // 3600} horas y {(tiempo_restante.seconds // 60) % 60} minutos...')
    
    # Esperar el tiempo especificado
    sleep(total_seconds)

    try:
        # Reproducir el sonido
        reproductor.music.load(sonido)
        reproductor.music.play()
        hablar("¡Es hora!")
        
        # Esperar hasta que se presione Enter para detener la alarma
        input("Presiona Enter para detener la alarma.")
        reproductor.music.stop()
    except pygame.error:
        hablar(f"Error al intentar cargar el archivo de sonido en la ruta: {sonido}")




##estructura de control
def principal():
        x= True
        hablar ("Hola, bienvenido a tu asistente personal ¿En qué puedo ayudarte?")
        while x:
            pedido= escuchar()

            if 'Hola' in pedido or 'hola' in pedido: #comandos
                hablar("Hola, ¿Cómo esta?")
                continue        
            elif 'Adiós' in pedido or 'adios' in pedido or 'adiós' in pedido:
                hablar("Hasta luego")
                break
            elif 'dictado' in pedido or 'Dictado' in pedido:
                dictado()
                continue
            elif 'Informacion' in pedido or 'informacion' in pedido or 'información' in pedido:
                informacion()
                continue
            elif 'Estructura' in pedido or 'estructura' in pedido:
                estructura()
                continue
            elif 'tarea' in pedido or 'Tarea' in pedido:
                tarea()
                continue
            elif 'música' in pedido or 'Música' in pedido:
                spotify()
                continue
            elif 'texto' in pedido or 'Texto' in pedido:
                app()
                continue
            elif 'mensaje' in pedido or 'Mensaje' in pedido:
                web()
                continue
            elif 'tabla' in pedido or 'Tabla' in pedido:
                grafica()
                continue  
            elif 'msn' in pedido or 'Msn' in pedido:#comandos a los que responde
                mensaje()#llama la funcion dictado, def
                continue #continua el programa
            elif 'canción' in pedido or 'Canción' in pedido:#comandos a los que responde
                cancion()#llama la funcion dictado, def
                continue #continua el programa 
            elif 'fecha' in pedido or 'Fecha' in pedido:#comandos a los que responde
                fecha()#llama la funcion dictado, def
                continue #continua el programa
            elif 'hora' in pedido or 'Hora' in pedido:#comandos a los que responde
                obtener_hora()#llama la funcion dictado, def
                continue #continua el programa 
            elif 'clima' in pedido or 'Clima' in pedido:#comandos a los que responde
                f_tempe()#llama la funcion dictado, def
                continue #continua el programa  
            elif 'compu' in pedido or 'Compu' in pedido:#comandos a los que responde
                info_pc()#llama la funcion dictado, def
                continue #continua el programa   
            elif 'apagar' in pedido or 'Apagar' in pedido:#comandos a los que responde
                off()#llama la funcion dictado, def
                continue #continua el programa                                            
            elif 'noticias' in pedido or 'Noticias' in pedido:#comandos a los que responde
                obtener_noticias()#llama la funcion dictado, def
                continue #continua el programa  
            elif 'alarma' in pedido or 'Alarma' in pedido:#comandos a los que responde
                poner_alarma()#llama la funcion dictado, def
                continue #continua el programa  
##principal
principal()