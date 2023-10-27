# Remove um item de um dicionário
livros = {
    'COD345' : '1984 - George Orwell',
    'COD222' : 'Dom Quixote de la Mancha - Miguel de Cervantes',
    'COD455' : 'O Pequeno Príncipe - Antoine de Saint-Exupéry',
    'COD875' : 'Dom Casmurro - Machado de Assis',
}

livros.pop('COD222')
print(livros.keys())