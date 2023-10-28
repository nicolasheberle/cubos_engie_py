# Escreva uma função que recebe a temperatura em Fahrenheit (f) e retorna a temperatura correspondente em Celsius (C) usando a fórmula a seguir:
# C = (f-32) * (5/9)

def conversao(f):
    c = (f - 32) * (5/9)
    return(c)
print(conversao(100))