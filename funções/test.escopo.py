# #Dentro de um programa python teremos:
# • Variáveis Globais: podem ser acessadas
# em qualquer momento no código, a
# partir do momento em que foi declarad
# • Variáveis Locais: só podem ser
# acessadas dentro da função em que ela
# foi declarada


idade_glob = 23
def calc_idade (ano_nasc, ano_atual): 
   idade_loc = ano_atual - ano_nasc
   return(idade_loc)