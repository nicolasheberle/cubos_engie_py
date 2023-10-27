# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.
# Criação das três variáveis solicitadas
a = 1
b = 2
c = 3

# Comparador para ver ficar qual a ordem correta das variáveis
if (a > b) and (a > c):
    primeiro = a
    if b > c:
        segundo = b
        terceiro = c
    else:
        segundo = c
        terceiro = b
elif (b > a) and (b > c):
    primeiro = b
    if a > c:
        segundo = a
        terceiro = c
    else:
        segundo = c
        terceiro = a
else:
    primeiro = c
    if a > b:
        segundo = a
        terceiro = b
    else:
        segundo = b
        terceiro = a
        
# Utilizando o print para imprimir o resultado da forma solicitada
print(primeiro,segundo,terceiro)