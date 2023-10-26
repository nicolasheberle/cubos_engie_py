# Você está trabalhando em contato com o setor de marketing e atualmente eles utilizam o seguinte texto para a apresentação aos investidores
# e precisam checar se todos as ideias chave foram mencionadas:
# Neste sentido, o entendimento das metas propostas nos obriga à análise do remanejamento dos quadros funcionais. Por outro lado, a percepção das dificuldades oferece uma interessante oportunidade para verificação dos métodos utilizados na avaliação de resultados. Assim mesmo, a consolidação das estruturas promove a alavancagem dos relacionamentos verticais entre as hierarquias. A nível organizacional, a necessidade de renovação processual cumpre um papel essencial na formulação das posturas dos órgãos dirigentes com relação às suas atribuições. Caros amigos, o novo modelo estrutural aqui preconizado garante a diversos militantes agrega valor ao estabelecimento dos modos de operação convencionais. Acima de tudo, é fundamental  Acima de tudo, é fundamental ressaltar que a constante divulgação das informações facilita a criação do sistema de formação de quadros que corresponde às necessidades. Nunca é demais lembrar o peso e o significado destes problemas, uma vez que a complexidade dos estudos efetuados é uma das consequências das condições inegavelmente apropriadas.

# Palavras
# -Nível Organizacional
# -Divulgação das Informações
# -Frequência de Publicações
# -Remanejamento dos Quadros

# Declare uma variável para guardar a informação do texto;
txt = 'Neste sentido, o entendimento das metas propostas nos obriga à análise do remanejamento dos quadros funcionais. Por outro lado, a percepção das dificuldades oferece uma interessante oportunidade para verificação dos métodos utilizados na avaliação de resultados. Assim mesmo, a consolidação das estruturas promove a alavancagem dos relacionamentos verticais entre as hierarquias. A nível organizacional, a necessidade de renovação processual cumpre um papel essencial na formulação das posturas dos órgãos dirigentes com relação às suas atribuições. Caros amigos, o novo modelo estrutural aqui preconizado garante a diversos militantes agrega valor ao estabelecimento dos modos de operação convencionais. Acima de tudo, é fundamental  Acima de tudo, é fundamental ressaltar que a constante divulgação das informações facilita a criação do sistema de formação de quadros que corresponde às necessidades. Nunca é demais lembrar o peso e o significado destes problemas, uma vez que a complexidade dos estudos efetuados é uma das consequências das condições inegavelmente apropriadas.'

# Declare uma varivável para cada palavra a ser buscada;
p1 = 'Nível Organizacional'
p2 = 'Divulgação de Informações'
p3 = 'Frequência de Publicações'
p4 = 'Remanejamento de Quadros'

# Imprima na tela para todas as variáveis se elas estão ou não presentes no texto;
#transformar tudo em letra minúscula
txt = txt.lower ()
p1 = p1.lower()
p2 = p2.lower()
p3 = p3.lower()
p4 = p4.lower()
print(p1 in txt)
print(p2 in txt)
print(p3 in txt)
print(p4 in txt)