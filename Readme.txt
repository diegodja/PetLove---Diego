PetLove - Analise Churn

Os dados foram separados em dois dataframes inicialmente: Deletados e Churn
Deletados são os dados de assinaturas canceladas e apenas essas considerando logicamente, a data de cancelamento (deleted_at). 
Churn são os dados de assinaturas criadas.

Os dois dataframes são novamente unidos no dataframe Churn. 

E então valores acumulativos de novas assinaturas e assinaturas canceladas são construídas para então replicar o Indicador Churn e iniciar sua análise. 

A partir da constatação da elevação nos valores do indicador, é atacada as variáveis que constroem seus valores. Assinaturas novas e canceladas, observando a regressão linear, para mensurar o quão progressivo está sendo.

Novos assinantes são valores constantes
Assinaturas canceladas mostram o motivo do indicador apresentar uma piora no valores, então focamos na identificação do porque.
Um dos pontos poderia ser o ticket médio, indicando um aumento nos preços, pela matérias primas mais caras na pandemia. Teoria descarta na observação dos valores de ticket médio constantes ao longo do tempo.
Analisando o período de inatividade de compras nas assinaturas, vimos que essa variável apresenta valores altos para os casos cancelados. Ou seja, as assinaturas são canceladas por inatividade. O gráfico construído em boxplot mostra a mediana para o status de assinaturas canceladas com bem acima dos outros status.
Então reduzir a inatividade já reduziria o cancelamento.
Fidelizar tornaria valores bem menos sucetíveis a mudanças bruscas, como a que esta ocorrendo. 
E tempos de crise também mostram oportunidades, Então casais que pensavam em ter filhos, já reconsideram a criação de um pet.
O código é bastante simples e lida apenas com regressões lineares, por simplicidade e apresentar valores de tendência através da inclinação da reta projetada. 

