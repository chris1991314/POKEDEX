# Con el lenguaje de programación Python, usando la librería requests y equipando las habilidades que has adquirido en este Módulo construirás 
# una Pokédex obteniendo los datos de https://pokeapi.co/
# Cuando el usuario introduzca el nombre de un Pokémon, si no existe que le mande un mensaje de error; si existe, 
# que muestre una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos). 
# Posteriormente, guardarás toda la información del pokémon (junto con el link de la imagen frontal del pokémon) 
# en un archivo .json dentro de una carpeta llamada “pokedex”.

import requests  #Para realizar solicitudes HTTP a la API de PokeAPI.
import os   #Para manejar directorios.
import json #Para guardar los datos en formato JSON.
import pandas as pd #Para crear archivos CSV.
import matplotlib.pyplot as plt # (de Pillow) para mostrar imágenes.
from PIL import Image
from io import BytesIO  # Para manejar datos binarios de la imagen.

def obtener_datos_pokemon(nombre_pokemon):  
    '''Realiza la solicitud a la PokeAPI para obtener la información del Pokémon y la muestra en la consola.'''
    # Realizar solicitud a la API
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        
        # Obtener datos necesarios
        nombre = datos_pokemon['name']
        peso = datos_pokemon['weight']
        altura = datos_pokemon['height']
        movimientos = [movimiento['move']['name'] for movimiento in datos_pokemon['moves']]
        habilidades = [habilidad['ability']['name'] for habilidad in datos_pokemon['abilities']]
        tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]
        url_imagen = datos_pokemon['sprites']['front_default']
        
        # Mostrar la información
        print(f"Nombre: {nombre}")
        print(f"Peso: {peso}")
        print(f"Altura: {altura}")
        print(f"Movimientos: {', '.join(movimientos)}")
        print(f"Habilidades: {', '.join(habilidades)}")
        print(f"Tipos: {', '.join(tipos)}")
        print(f"URL de la imagen: {url_imagen}")
        
        # Mostrar la imagen del Pokémon
        mostrar_imagen(url_imagen)

        # Guardar la información en archivos JSON y CSV
        guardar_datos_pokemon(nombre, peso, altura, movimientos, habilidades, tipos, url_imagen)
        '''Crea un archivo .json y un archivo .csv con la información del Pokémon 
        en una carpeta llamada pokedex utilizando pandas para estructurar los datos.'''
        
    else:
        print("Error: Pokémon no encontrado.")

def mostrar_imagen(url_imagen):
    # Realizar la solicitud para obtener la imagen
    respuesta_imagen = requests.get(url_imagen)
    imagen = Image.open(BytesIO(respuesta_imagen.content))
    
    # Mostrar la imagen utilizando matplotlib
    plt.imshow(imagen)
    plt.axis('off')  # Ocultar los ejes
    plt.show()

def guardar_datos_pokemon(nombre, peso, altura, movimientos, habilidades, tipos, url_imagen):
    # Crear carpeta "pokedex" si no existe
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')
    
    # Crear el diccionario con la información del Pokémon
    informacion_pokemon = {
        'nombre': nombre,
        'peso': peso,
        'altura': altura,
        'movimientos': movimientos,
        'habilidades': habilidades,
        'tipos': tipos,
        'url_imagen': url_imagen
    }
    
    # Guardar la información en un archivo JSON
    ruta_json = os.path.join('pokedex', f"{nombre}.json")
    with open(ruta_json, 'w') as archivo_json:
        json.dump(informacion_pokemon, archivo_json, indent=4)
    
    print(f"Información guardada en {ruta_json}")
    
    # Guardar la información en un archivo CSV usando pandas
    df = pd.DataFrame({
        'nombre': [nombre],
        'peso': [peso],
        'altura': [altura],
        'movimientos': [', '.join(movimientos)],
        'habilidades': [', '.join(habilidades)],
        'tipos': [', '.join(tipos)],
        'url_imagen': [url_imagen]
    })
    
    ruta_csv = os.path.join('pokedex', f"{nombre}.csv")
    df.to_csv(ruta_csv, index=False)
    print(f"Información guardada en {ruta_csv}")

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    obtener_datos_pokemon(nombre_pokemon)

if __name__ == "__main__":    #  main: Función principal que solicita al usuario el nombre del Pokémon y llama a obtener_datos_pokemon.
    main()

GRACIAS POR EL CURSO MUY BUENO HE APRENDIDO MUCHO Y CONVINADO CON LOS CONOCIMIENTO QUE HE ADQUIRIDO EN ESTE CUATRIMESTRE EN MI UNIVERSIDAD HE COMPLEMENTADO MIS CONOCIMIENTOS SEGUIRE ESFORZANDOME AL MAXIMO. 
