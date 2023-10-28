# Escreva uma função que recebe uma string e retorna True caso o texto esteja escrito em maiúsculo e False caso contrário
def maiusculo(txt):
    t_m = txt.upper()
    condicao = (t_m == txt)
    return(condicao)

print(maiusculo('PAO'))
print(maiusculo('pao'))