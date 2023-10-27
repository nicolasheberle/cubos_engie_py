# Os valores máximos aceitáveis de colesterol variam de acordo com características individuais. Sabe-se que idosos, fumantes e cardiopatas
# devem manter seu colesterol LDL abaixo de 70, já pacientes sem nenhuma doença devem manter o colesterol abaixo de 130.
# Crie um código que recebe a informação se a pessoa é idosa, fumante ou cardiopata, seu nível de colesterol e retorne "SAUDÁVEL" caso os
# níveis estejam dentro do recomendado ou "NÃO SAUDÁVEL".

# Criando as variáveis necessárias para a resolução do exercício
ldl = 45
comorbidade = True

if comorbidade:
    if ldl < 70:
        print('SAUDÁVEL')
    else:
        print('NÃO SAUDÁVEL')
else:
    if ldl < 130:
        print('SAUDÁVEL')
    else:
        print('NÃO SAUDÁVEL')
