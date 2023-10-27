# Faça um código que imprima o produto mais barato do cardápio, e seu valor
# mbn = mais_barato_nome
# mbv = mais_barato_valor
mbn = ''
mbv = float('inf')
# Cardápio
cardapio = {
    'strogonoff': 34.99,
    'churrasco': 74.99,
    'risoto': 39.99,
    'pizza': 44.99
}
# Encontra o produto mais barato e seu valor
for produto, valor in cardapio.items():
    if valor < mbv:
        mbv = valor
        mbn = produto
        
if mbn:
    print(f'O produto mais barato é {mbn} com o valor de R${mbv:.2f}')
else:
    print('O cardápio está vazio.')