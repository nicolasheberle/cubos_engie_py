# Crie uma função que retorne o menor dos elementos de uma lista para as seguintes listas
# . [3,4,5,8,7,10,2,5,8,9,10]
# . [3,4,5,8, 7, 10, 2,5,8,9,10,800]

def min(lista):
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return(menor)
    
minha_lista1 = [3,4,5,8,7,10,2,5,8,9,10]
minha_lista2 = [3,4,5,8, 7, 10, 2,5,8,9,10,800]

print(min(minha_lista1), min(minha_lista2))