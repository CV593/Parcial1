#Define una función llamada "inverso_palabra" que reciba una cadena como parámetro y devuelva la 
# cadena invertida. Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".

def inverso_palabra(palabra):
    return palabra[::-1]

palabra = "Python"

print(f"Palabra Orginal {palabra}")
print(f"Palabra Invertida {inverso_palabra(palabra)}")
