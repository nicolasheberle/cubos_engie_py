# Operador f-string, que inclui a inserção de um texto e imbuir nele variáveis ou vice e versa. 
x = 'pão'
y = 'de'
z = 'alho'
n = 'churrasco'
a = x+' '+y+' '+ z 
print(x,y,z,n) #dessa forma está claro de que se trata de um pão de alho e um churrasco, porém está confuso por não contexto e ou sentido.
print(f'Eu gosto muito de {x} {y} {z} com {n}') #claro se eu fizer uma variável que junte x,y,z diminuiria o código.
print(f'Eu gosto muito de {a} com {n}') #assim o código fica mais enxuto.