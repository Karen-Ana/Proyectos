from pyperclip import copy as portapapeles
print("¿Que quieres guardar en el portapapeles?")
contenido = input()
portapapeles(contenido)
print("El texto se guardo satisfactoriamente en el portapapeles")