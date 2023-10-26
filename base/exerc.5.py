# 1.Declarar uma variável com um número qualquer
# 2.Como descobrir se essa variável contém um número par ou ímpar?

x = 15
m_x = x % 2 #& calcula o resto da divisão
print(m_x)
if m_x == 1:
  print('impar')
else:
  print('par')
