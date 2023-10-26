# Replace operador de realocação dentro de uma variável
txt = 'Eu gosto de comer purê de batata, frango a milanesa e arroz, com soda de cola.'
print(txt) #sem edição
print(txt.replace('frango', 'bife de gado')) #editado a proteína sem alterar a variavel
txt = txt.replace('purê de batata', 'batata frita') #editando a batata e alterando a variavel
print(txt)