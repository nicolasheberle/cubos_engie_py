# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando pares chave-valor ao dicionário
meu_dicionario['chave1'] = 'valor1'
meu_dicionario['chave2'] = 'valor2'

# Acessando valores por suas chaves
print(meu_dicionario['chave1'])  # Saída: 'valor1'

# Verificando se uma chave existe no dicionário
if 'chave3' in meu_dicionario:
    print(meu_dicionario['chave3'])
else:
    print('A chave3 não existe no dicionário.')

# Iterando pelos pares chave-valor em um dicionário
for chave, valor in meu_dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')