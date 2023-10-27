# Crie um dicionário que armazena dados para cada produto, com os seguintes campos:
# • Nome (String)
# • Tipo (Número)
# • Preço (Número)
# Declare 3 produtos da sua escolha usando esse formato de dicionário.
# Esses produtos precisam estar em uma lista.
prod1 = {
    'nome' :  'Suporte de Monitor',
    'tipo' : 1,
    'preço' : 79.99
}
prod2 = {
    'nome' : 'Monitor Curvo Oled 4k 280Hz',
    'tipo' : 1,
    'preço' : 119.99
}
prod3 = {
    'nome' : 'RTX 9090 2TB Ram',
    'tipo' : 2,
    'preço' : 99.99
}
produtos = [prod1, prod2, prod3]
# print(produtos)

# Precisamos agora adicionar 2 produtos nessa lista:
# Mouse Gamer, 2 (tipo), R$56,00
# Mouse Pad, 2 (tipo), R$32,90

produtos.append({'nome' : 'Mouse gamer',
                 'tipo' : 2,
                 'preço' : 56.00})
produtos.append({'nome' : 'Mouse pad',
                 'tipo' : 2,
                 'preço' : 32.90})
# print(produtos)

# Percebemos que esses produtos não tem um identificador único. Adicione uma propriedade chamada código em cada produto, passando um número maior que 100, que seja único, ou seja, não se repita.
contador_codigo = 101

for prod in produtos:
    prod['código'] = contador_codigo
    contador_codigo += 1
# print(produtos)

# Descobrimos que o melhor jeito de guardar as informações não é em listas, mas em um dicionário de dicionários, onde a chave é o código do produto. Usando loops faça essa transformação até ficar no seguinte formato:
# produtos = {
#     100 : {
#         'nome' : 'Suporte de monitor',
#         'tipo' : 1,
#         'preço' : 54.98
#     }
# }
novos_produtos = {}

for prod in produtos:
    cod = prod['código']
    prod.pop('código')
    novos_produtos[cod] = prod

print(novos_produtos)