from pyperclip import copy as portapapeles
from wikipedia import set_lang as idioma, page as buscar, search

# Configurar idioma de Wikipedia
idioma("es")

# Solicitar el tema de búsqueda
print("¿Qué tema quieres buscar?")
clave = input()

try:
    # Buscar el tema en Wikipedia
    resultados = search(clave)
    if resultados:
        respuesta = buscar(resultados[0])  # Obtener la primera página de los resultados

        # Mostrar y guardar el contenido en el portapapeles
        titulo = f"Título: {respuesta.title}"
        resumen = f"Contenido: {respuesta.content}"
        print(titulo)
        print(resumen)

        # Combinar título y resumen para guardar en el portapapeles
        contenido = f"{titulo}\n\n{resumen}"
        portapapeles(contenido)
        print("El texto se guardó satisfactoriamente en el portapapeles.")
    else:
        print("No se encontraron resultados para la búsqueda.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
