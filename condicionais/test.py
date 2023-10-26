#Condicionais
# • Se idade => 18, então faixa etária = adulto
idade = 20

if idade >= 18:
    faixa_etaria = "adulto"
else:
    faixa_etaria = "outros"
print(faixa_etaria)

# • Se modo de pagamento = à vista, então desconto
modo_pagamento = 'à vista'

if modo_pagamento == 'à vista':
    desconto = True
else:
    desconto = False
print(desconto)

# • Se nível de chuva > 0, então não lavar roupa
chuva = 50

if chuva > 0:
    lavar_roupa = False
else:
    lavar_roupa = True
print(lavar_roupa)

# • Se distância > 500km, então dormir na viagem

distancia = 501

if distancia > 500:
    dormir = True
elif distancia <= 500:
    dormir = False
print(dormir)

