# Crie uma função que calcule a média dos elementos de uma lista para as seguintes listas:
# . [3,4,5,8,7,10,2,5,8,9,10]
# . [3,4,5,8, 7, 10, 2,5,8,9,10,800]
# x = (x₁+x₂+...+xn)/n, onde n representa o número de elementos

def media(lista):
    n = len(lista)
    soma = 0
    for item in lista:
        soma += item
    media = soma / n
    return(media)

minha_lista1 = [3,4,5,8,7,10,2,5,8,9,10]
minha_lista2 = [3,4,5,8, 7, 10, 2,5,8,9,10,800]

print(media(minha_lista1), media(minha_lista2))