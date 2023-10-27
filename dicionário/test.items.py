# Retorna todas as chaves e valores de um dicionário como uma lista de listas
livros = {
    'COD345' : '1984 - George Orwell',
    'COD222' : 'Dom Quixote de la Mancha - Miguel de Cervantes',
    'COD455' : 'O Pequeno Príncipe - Antoine de Saint-Exupéry',
    'COD875' : 'Dom Casmurro - Machado de Assis',
}

livros.pop('COD222')
livros.pop('COD455')
print(livros.items())