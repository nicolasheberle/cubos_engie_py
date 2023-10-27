# Teste operador lógico simples
#Exemplo-Escola
# Um aluno passa de ano se:
#  • Nota final ≥ 6
#  • Presença ≥ 75%
nota = 5
presenca = 80
if (nota >= 6) and (presenca >= 75): #compara ambas as variáveis para ver se é true ou false a sentença.
    status = 'aprovado'
else: #caso o if de o resultado false, o else entra em ação e executa o comando que estiver abaixo.
    status = 'reprovado'
print (status)