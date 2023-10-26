# Exemplo Escola
#  • Se nota final >= 7, o aluno é aprovado
#  Caso contrário:
#  • Se nota final >= 3, o aluno fica de recuperação
#  • Caso contrário, o aluno é reprovado
nota = 2
if nota >= 7:
 status = 'aprovado'
else:
    if nota >= 3:
        status= 'recuperação'
    else:
        status = 'reprovado'
print (status)