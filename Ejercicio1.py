# Escribe una función en Python que reciba una lista 
# como parámetro y devuelva la suma de todos los elementos de la lista. 

def sum_lista(list):
    sum = 0
    for e in list:
        sum += e
    return sum
list=[1,2,3,4,5,6,7,8,9,10]

print(f"La lista es {list}")
print(f"Su suma es {sum_lista(list)}")