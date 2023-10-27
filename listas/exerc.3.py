# Faça um programa que conta quantas letras "a" existem numa determinada palavra. Imprima o resultado na tela
palavra = 'palavra'
conta = 0

for letra in palavra:
    if letra == 'a':
        conta = conta + 1
    
print(conta)