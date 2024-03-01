#Escribe un programa que pida al usuario una lista de números y 
# luego imprima la suma de los números pares en la lista.

entrada = input("Ingrese los numeros de la lista (separados por espacio): ")
numeros = [int(numero) for numero in entrada.split()]
def sumar_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

print(f"La lista es {numeros}")
print(f"La suma de los números pares es {sumar_pares(numeros)}")