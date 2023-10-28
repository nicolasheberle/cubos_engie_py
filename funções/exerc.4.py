# Escreva uma função que recebe um número inteiro positivo e:
#     1.Teste se ele é de fato inteiro e positivo
# Se não, retorna uma mensagem de erro
#     2.Retorne em uma lista todos os seus divisores

def f_1(num):
    # Testando se é inteiro
    inteiro = int(num)
    cond1 = (inteiro == num)
    # Testando se é positivo
    cond2 = (num > 0)
    # Retorna True caso as duas sentanças sejam atendidas ou False caso ao menos uma não seja
    return(cond1 & cond2)

def f_2(num):
    divisores = []
    indicador = 1
    while indicador <= num:
        if num % indicador == 0:
            divisores.append(indicador)
        indicador += 1
    return(divisores)

print(f_2(14))

def f_f(num):
    if f_1(num) == True:
        divisores = f_2(num)
        return(divisores)
    else:
        print('Seu número não é inteiro e positivo')