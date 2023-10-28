# Escreva uma função que recebe um número inteiro positivo e retorna:
# • o número de dígitos que ele possui
# • seu primeiro dígito

def digitos(num):
    txt = str(num)
    num_digitos = len(txt)
    primeiro_digito = txt[0]
    return(num_digitos, primeiro_digito)

print(digitos(1024))