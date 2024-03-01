#Crea un diccionario en Python que represente un libro, con claves como "título", "autor" y "año de 
# publicación". Luego, escribe un código que agregue un nuevo campo al diccionario, como "género", y 
# lo imprima.

dic = {
    'Titulo': "CRIMEN Y CASTIGO",
    'Autor': "FYODOR DOSTOYEVSKI",
    'Anio_Publicacion': 1890,
    "ISBN":  123456789
}

dic["Genero"] = "Novela"
print("LOS DATOS DEL DICCIONARIO SON:\n")
print(dic)
print("\nYA ORDENADOS SON:")
print(f"\nTitulo: {dic['Titulo']}")
print(f"Autor: {dic['Autor']}")
print(f"Año de Publicacion: {dic['Anio_Publicacion']}")
print(f"ISBN: {dic['ISBN']}")
print(f"Genero: {dic['Genero']}")
