import requests

ciudad = input("Ciudad: ")
url = f"https://wttr.in/{ciudad}?format=%t"

response = requests.get(url)

# Verificar si la respuesta contiene "°C"
if "°C" in response.text:
    temp_celsius = float(response.text.strip().replace("°C", ""))
    print(f"Estamos a {temp_celsius}°C en {ciudad}.")
else:
    print("No se pudo obtener la temperatura. Verifica la ciudad o el servicio.")
