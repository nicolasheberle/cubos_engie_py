# 1. Declare uma variável cardapio, que tem como conteúdo um dicionário que armazena os dados de comidas e preços, para o cardápio de  um restaurante. Onde o nome do prato é a chave e o valor o preço a ser pago.
# 2. Escreva 4 pratos com seus valores dentro do cardápio.
# Cardápio
cardapio = {
    'strogonoff' : 34.99,
    'churrasco' : 74.99,
    'risoto' : 39.99,
    'pizza' : 44.99
}
# 3.Exiba na tela todos os produtos com seus preços no seguinte formato: lasanha: R$43.98
for item in cardapio:
    print(f'{item}: R$ {cardapio[item]}')
# 4. Adicione mais 2 produtos da sua escolha ao cardapio
cardapio['pudim'] = 6.99
cardapio['bebida'] = 9.99