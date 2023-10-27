# • Laço com quantidade indeterminada de repetições
# • Repetição acontece quando uma condição é satisfeita
# • Exemplo de Aplicação: Enquanto determinada condição é satisfeita, repita determinado comando
repetir = True
alvo = 5

while (repetir):
    digitado = input('Digite um número de 1 a 10: ')
    print('Digitou: ' + digitado)
    if (int(digitado) == alvo):
        print('Acertou!')
        repetir = False
    else:
        print('Errou, tente novamente :/')
