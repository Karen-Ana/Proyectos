import requests
from bs4 import BeautifulSoup

def obtener_noticias_el_pais():
    url = "https://elpais.com/"
    
    # Realizar la solicitud a la página web
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(respuesta.text, "html.parser")
        
        # Buscar titulares (en este caso, están en etiquetas <h2>)
        titulares = soup.find_all("h2", class_="c_t")
        
        if titulares:
            print("Noticias principales de El País:")
            for i, titular in enumerate(titulares[:10], 1):  # Obtener los primeros 10 titulares
                print(f"{i}. {titular.get_text(strip=True)}")
        else:
            print("No se encontraron titulares.")
    else:
        print(f"Error al acceder a la página: {respuesta.status_code}")

# Llamar a la función para mostrar las noticias
obtener_noticias_el_pais()
