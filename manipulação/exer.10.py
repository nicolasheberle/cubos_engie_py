# O time com o qual você está trabalhando estava revisando um texto que precisava ser enviado urgente para um cliente e perceberam que
# existe um erro de digitação que acontece várias vezes ao longo do email. Eles precisam da sua ajuda para corrigir o texto:

# O cuiddo em identificar ponts críticos na estrutura atual da organização deve passar por modificações independentemente do
# processo de comunicação como um todo. Desta maneira, o aumento do diálogo entre os diferentes setores produtivos causa
# impacto indireto na reavaliação das formas de ação. No entanto, não podemos esquecer que a crescente influência da mídia
# apresenta tendências no centido de aprovar a manutenção de alternativas às soluções ortodoxas.
# É claro que a execução dos ponts do programa representa uma abertura para a melhoria do cuiddo das direções preferenciais
# no centido do progresso. Podemos já vislumbrar o modo pelo qual a expansão dos mercados mundiais maximiza as
# possibilidades por conta do investimento em reciclagem técnica. A certificação de metodologias que nos auxiliam a lidar com o
# julgamento imparcial das eventualidades exige o cuiddo e a precisão e a definição das condições financeiras e administrativas
# exigidas.

# Palavras a serem corrigidas:
# errada: ponts, centido e cuiddo
# correta: pontos, sentido e cuidado

# Declare uma variável para guaradar o texto;
# Utilize o replace para substituir as palavras erradas;
# Substitua o valor da variável existente pelo novo resultado;
# Repita até que todas as palavras tenham sido corrigidas

txt = 'O cuiddo em identificar ponts críticos na estrutura atual da organização deve passar por modificações independentemente doprocesso de comunicação como um todo. Desta maneira, o aumento do diálogo entre os diferentes setores produtivos causaimpacto indireto na reavaliação das formas de ação. No entanto, não podemos esquecer que a crescente influência da mídiaapresenta tendências no centido de aprovar a manutenção de alternativas às soluções ortodoxas.É claro que a execução dos ponts do programa representa uma abertura para a melhoria do cuiddo das direções preferenciaisno centido do progresso. Podemos já vislumbrar o modo pelo qual a expansão dos mercados mundiais maximiza aspossibilidades por conta do investimento em reciclagem técnica. A certificação de metodologias que nos auxiliam a lidar com ojulgamento imparcial das eventualidades exige o cuiddo e a precisão e a definição das condições financeiras e administrativas exigidas.'
txt = txt.lower()

txt = txt.replace ('ponts', 'pontos')
txt = txt.replace('centido','sentido')
txt = txt.replace('cuiddo', 'cuidado')

print(txt)