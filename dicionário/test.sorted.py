#
livros = {
    'COD345' : '1984 - George Orwell',
    'COD222' : 'Dom Quixote de la Mancha - Miguel de Cervantes',
    'COD455' : 'O Pequeno Príncipe - Antoine de Saint-Exupéry',
    'COD875' : 'Dom Casmurro - Machado de Assis',
}
print (sorted (livros))
for i in sorted (livros):
    print(f'{i} -> {livros[i]}')