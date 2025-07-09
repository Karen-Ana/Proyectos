from wikipedia import set_lang as idioma
from wikipedia import page as buscar

idioma("es")

print("Que tema quieres buscar....")
clave = input()
respuesta = buscar("clave")

print(f"Titulo: {respuesta.title}")
print(f"Contenido: {respuesta.summary}")