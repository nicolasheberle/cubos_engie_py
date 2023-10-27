# • Laço com quantidade determinada de repetições
# • Repetição acontece ao longo de uma lista
# • Exemplo de Aplicação:
# Para todos os elementos de determinado conjunto, repita determinado comando
vogais = ['a', 'e', 'i', 'i', 'o', 'u']
for letra in vogais:
    maiuscula = letra.upper() # Modificar a variável para maiúscula antes de ser imprimida
    print(maiuscula)

# Realizar dentro um loop
notas = [6.4, 7, 9, 10, 10, 5, 10, 8]
for nota in notas:
    passou = (nota >= 7)
    print (passou)
