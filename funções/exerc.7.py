# Escreva uma função que recebe um número inteiro positivo menor ou igual que 10 e retorne o número escrito por extenso.

def numero_por_extenso(numero):
    numeros_extenso = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez"]

    if 0 <= numero <= 10:
        return numeros_extenso[numero]
    else:
        return "Número fora do intervalo permitido."

# Exemplos de uso:
numero = 5
print(f"{numero} por extenso: {numero_por_extenso(numero)}")

numero = 10
print(f"{numero} por extenso: {numero_por_extenso(numero)}")