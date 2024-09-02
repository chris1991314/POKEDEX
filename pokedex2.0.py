import requests
from tkinter import Tk, Label, Entry, Button, StringVar, Frame
from PIL import Image, ImageTk
from io import BytesIO

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos['name'].capitalize()
        altura = datos['height'] / 10
        peso = datos['weight'] / 10
        tipos = ", ".join([tipo['type']['name'].capitalize() for tipo in datos['types']])
        imagen_url = datos['sprites']['front_default']
        
        return nombre, altura, peso, tipos, imagen_url
    else:
        return None

def mostrar_pokemon():
    nombre_pokemon = entrada_nombre.get()
    datos = obtener_datos_pokemon(nombre_pokemon)
    
    if datos:
        nombre, altura, peso, tipos, imagen_url = datos
        etiqueta_nombre.config(text=f"Nombre: {nombre}")
        etiqueta_altura.config(text=f"Altura: {altura} m")
        etiqueta_peso.config(text=f"Peso: {peso} kg")
        etiqueta_tipos.config(text=f"Tipos: {tipos}")
        
        # Obtener y mostrar la imagen
        imagen_respuesta = requests.get(imagen_url)
        imagen_pokemon = Image.open(BytesIO(imagen_respuesta.content))
        imagen_pokemon = imagen_pokemon.resize((150, 150), Image.ANTIALIAS)
        imagen_tk = ImageTk.PhotoImage(imagen_pokemon)
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk
    else:
        etiqueta_nombre.config(text="Pokémon no encontrado.")
        etiqueta_altura.config(text="")
        etiqueta_peso.config(text="")
        etiqueta_tipos.config(text="")
        etiqueta_imagen.config(image='')

# Configuración de la ventana principal de Tkinter
ventana = Tk()
ventana.title("Pokédex")
ventana.geometry("300x400")

frame = Frame(ventana)
frame.pack(pady=10)

entrada_nombre = StringVar()
entry = Entry(frame, textvariable=entrada_nombre, font=("Arial", 14))
entry.pack(side="left")

boton_buscar = Button(frame, text="Buscar", command=mostrar_pokemon)
boton_buscar.pack(side="left", padx=10)

etiqueta_nombre = Label(ventana, text="", font=("Arial", 14))
etiqueta_nombre.pack()

etiqueta_altura = Label(ventana, text="", font=("Arial", 14))
etiqueta_altura.pack()

etiqueta_peso = Label(ventana, text="", font=("Arial", 14))
etiqueta_peso.pack()

etiqueta_tipos = Label(ventana, text="", font=("Arial", 14))
etiqueta_tipos.pack()

etiqueta_imagen = Label(ventana)
etiqueta_imagen.pack(pady=10)

ventana.mainloop()
