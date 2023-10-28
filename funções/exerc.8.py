# Crie uma função que ordena em ordem crescente os valores de uma lista e retorna uma lista com o valor mínimo e máximo, para as seguintes listas:
# • [3,4,5,8,7,10,2,5,8,9,10]
# • [3,4,5,8,7,10,2,5,8,9,10,800]

def min_max_ordem(lista):
    lista_ordenada = sorted(lista)  # Ordena a lista em ordem crescente
    valor_min = lista_ordenada[0]  # Primeiro elemento é o mínimo
    valor_max = lista_ordenada[-1]  # Último elemento é o máximo
    return [valor_min, valor_max]

# Exemplos de uso:
lista1 = [3, 4, 5, 8, 7, 10, 2, 5, 8, 9, 10]
resultado1 = min_max_ordem(lista1)
print(f"Lista 1: Valor mínimo: {resultado1[0]}, Valor máximo: {resultado1[1]}")

lista2 = [3, 4, 5, 8, 7, 10, 2, 5, 8, 9, 10, 800]
resultado2 = min_max_ordem(lista2)
print(f"Lista 2: Valor mínimo: {resultado2[0]}, Valor máximo: {resultado2[1]}")