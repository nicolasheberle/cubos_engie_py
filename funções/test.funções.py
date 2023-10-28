# Pedaço de código que realiza alguma tarefa específica:
# Podem ser chamadas em qualquer parte do programa
# • Quantas vezes desejarmos
# Deixa nosso programa mais limpo e organizado
# • Evita escrever código repetitivo
 
# def nome_funcao(arg1, arg2, ...):
#     comandos a serem executados
#     return( resultado da funcao)

# def soma(x, y):
#     resultado = x +y
#     return(resultado)
# print(soma(1,2))

# def introducao (nome, idade, altura, profissao):
#     print(f"Olá! Meu nome é {nome}, tenho {idade} anos, {altura}m de altura e sou {profissao}.")
# introducao("Nicolas", 20, 1.80, "Universitário em Ciência de Dados")

# def faixa_etaria(idade):
#     if idade <= 18:
#         fx_etaria = "Jovem"
#     elif idade <= 60:
#         fx_etaria = "Adulto"
#     else:
#         fx_etaria = "Idoso"
#     return(fx_etaria)
# print(faixa_etaria(50))

def soma(lista):
    total = 0
    for item in lista:
        total += item
    return(total)

minha_lista = [1,2,3,4]
print(soma(minha_lista))