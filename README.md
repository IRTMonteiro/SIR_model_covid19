# SIR_model_covid19
Objetivo: Aplicar o modelo epidemiológico SIR utilizado em epidemias de gripe/ebola/zika para analisar o surto de SARS-Cov2 pelas cidades baseado no número de infectados

# Modelor SIR 
Vamos modelar a dinâmica de uma doença (gripe, por exemplo), que se propaga numa certa população. Para isso, começamos por dividir a população em 3 grupos:

        * S = {Suscetíveis} - os que podem adquirir o vírus, mas que atualmente não estão infectados;
        * I = {Infectados} - os que estão infectados com o vírus e podem transmiti-lo a outros;
        * R = {Removidos/Recuperados} - os que não podem contrair o vírus, ou porque recuperaram permanentemente
                                    e ficaram imunes (pelo menos durante o período em análise), ou porque
                                    são naturalmente imunes ou porque morreram!

# Equações do modelo
O modelo SIR leva em conta um conjunto de três equações, que representam a taxa de variação dos grupos em função do tempo t: 

        *dS = beta * [ [S(t) * I (t)] / N ] * dt;
        *dI = { [{beta* S(t) * I(t)} / N] - gama * I(t) } * dt;
        *dR = - gama * I(t) * dt:



# Coeficientes do Modelo SIR
* Gama : Coeficiente de recuperação. É uma taxa per-capita e por unidade de tempo. O seu recíproco 1/γ, pode ser identificado como o tempo de residência, o tempo médio em que um indivíduo pode infectar outras pessoas. Para a gripe, o período é de 1 a 3 dias. Se o considerarmos igual a 2 dias (Média entre 1 e 3 dias), por exemplo, isto significa que a taxa de recuperação é γ = 1/2 (indivíduo por dia) e portanto em um dia metade dos infetados recuperam – passam para o grupo de recuperados R

* Beta : Coecifiente de transmissão. Suponhamos que cada indivduo entra em contato em média com C outros, escolhidos aleatoriamente. C diz-se a 'taxa de contato per-capita' por unidade de tempo. Considerando a hipótese de uma população homogeneamente misturada, C é constante. Se p é a probabilidade de que um contato resulte em contágio e, uma vez que existem I(t) indivíduos infetados no total, isso significa que o número de novas infeções, no intervalo de tempo é C \* p = beta. O coenficiente de transmissão depende do contato médio (C) entre indivíduos de uma população e a probabilidade (p) de um infectado infectar um individo saudável.

# Referência:
[1] https://rce.casadasciencias.org/rceapp/pdf/2017/020/
