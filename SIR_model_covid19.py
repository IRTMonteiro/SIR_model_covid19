import matplotlib.pyplot as plt

'''
 ================= Objetivo ====================
 Aplicar o modelo epidemiológico SIR utilizado em epidemias de gripe/ebola/zika 
 para analisar o surto de SARS-Cov2 pelas cidades baseado no número de infectados
 
 @__Author__: Conrado Ferreira Bittencourt
 + Informações na descrição da classe.
'''


class Doenca:
    '''
    Esta classe cria uma doença, que será iterada por um tempo  (em dias)
    considerando o modelo epidemiológico SIR

    ================= MODELO SIR ==================
    Vamos modelar a dinâmica de uma doença (gripe, por exemplo),
    que se propaga numa certa população. Para isso, começamos por dividir a população em 3 grupos:
        * S = {Suscetíveis} - os que podem adquirir o vírus, mas que atualmente não estão infectados;
        * I = {Infectados} - os que estão infectados com o vírus e podem transmiti-lo a outros;
        * R = {Removidos/Recuperados} - os que não podem contrair o vírus, ou porque recuperaram permanentemente
                                    e ficaram imunes (pelo menos durante o período em análise), ou porque
                                    são naturalmente imunes ou porque morreram!

    ==================   gama  ====================
    Gama: coeficiente de recuperação.
        É uma taxa per-capita e por unidade de tempo. O seu recíproco, 1/γ,
        pode ser identificado como o tempo de residência no compartimento infeccioso, isto é, o
        tempo médio em que um indivíduo pode infectar outras pessoas. Para a gripe, o período infecioso é
        tipicamente de 1 a 3 dias. Se o considerarmos igual a 2 dias, por exemplo, isto significa que a taxa
        de recuperação é γ = 1/2 (por indivíduo por dia) e portanto num dia metade dos infetados
        recuperam – passam para o compartimento R

    ==================   beta  ====================
    Beta: Coecifiente de transmissão.             Unidade: 1/tempo
        Suponhamos que cada indivduo contacta, por unidade de tempo, em média com C outros,
        escolhidos aleatoriamente. C diz-se a 'taxa de contacto per-capita' por unidade de tempo.
        Pela hipótese de uma população homogeneamente misturada, C é constante.
        Se p é a probabilidade de que um contacto resulte em contágio e, uma vez que
        existem I(t) indivíduos infetados no total, isso significa que o número de novas infeções, no intervalo de tempo
        é C*p = beta.

        Logo C*p respectivamente, correspondem a uma taxa de contacto c = 2
        e a uma probabilidade de contágio p=0.84 (Gripe por exemplo).

        (uma hipótese muito questionavel!... Mas razoável)

    ========= Equações do modelo SIR ===============

    dS = beta * [ [S(t) * I (t)] / N ] * dt
    dI = { [{beta* S(t) * I(t)} / N] - gama * I(t) } * dt
    dR = - gama * I(t) * dt

    referência: https://rce.casadasciencias.org/rceapp/pdf/2017/020/

    Criado por: Conrado Ferreira Bittencourt
    Gmail: conrad.bittencourt
    Data: 11/04/2020
    '''


    def __init__(self, populacao, beta, gama, tDeath, infectado=1, curado=0,
                 mortos=0, simulationTime=21, leitos=0):
        """

        :param populacao: População da cidade
        :param beta: Coecifiente de transmissão
        :param gama: Coeficiente de recuperação
        :param tDeath: Taxa de mortalidade
        :param infectado: Número inicial de infectados
        :param curado: Número inicial de curados
        :param mortos: Número de mortos
        :param simulationTime: Tempo de iteração
        :param leitos: Número de leitos total
        """

        self.simulationTime = simulationTime
        self.populacao = populacao
        self.beta = beta
        self.gama = gama
        self.tDeath = tDeath
        self.tDeath = tDeath * gama  # testar tDeath / gama
        self.tCuradas = gama * (1 - tDeath)

        # ====== variáveis ========
        self.I = [infectado / populacao]
        self.C = [curado / populacao]
        self.D = [mortos / populacao]
        self.S = [(populacao - infectado) / populacao]
        self.time = [0]
        self.leitos = [leitos]

    def run(self):
        """
        -> Executa a iteração do modelo SIR, com passo 0.01
        :return:
        """
        dt = 0.01

        # iterando
        for t in range(int(self.simulationTime / dt)):
            I = self.I[-1] + (self.beta * self.I[-1] * self.S[-1] - self.gama * self.I[-1]) * dt
            C = self.C[-1] + (self.tCuradas * self.I[-1]) * dt
            D = self.D[-1] + (self.tDeath * self.I[-1]) * dt  # (1 - (self.I[-1])/ 774 )
            S = self.S[-1] - (self.beta * self.I[-1] * self.S[-1]) * dt
            time = self.time[-1] + dt

            self.I.append(I)
            self.C.append(C)
            self.D.append(D)
            self.S.append(S)
            self.time.append(time)
            self.leitos.append(744)

        # Colocando em número absoluto
        self.I = [i * self.populacao for i in self.I]
        self.C = [c * self.populacao for c in self.C]
        self.D = [d * self.populacao for d in self.D]
        self.S = [s * self.populacao for s in self.S]

    def plot(self, mortalidade, contato, probabilidade):

        """
        -> Escreve os dados de Run em um gráfico
        :param mortalidade: Mortalidade que será impressa no gráfico
        :param contato: Contato médio entre pessoas que será impresso no gráfico
        :param probabilidade: Probabilidade de infecção entre duas pessoas que será impresso no gráfico.
        :return:
        """

        self.mortalidade = mortalidade
        self.contato = contato
        self.probabilidade = probabilidade

        plt.title("Projeção infectados SARS-COV2 2020\n"
                  "Controle por Isolamento\n"
                  "Curitiba, considerando boletim SESA 19/03 : 17 confirmados")

        plt.xlabel('Dias \n\n'
                   ' Contato social médio: {} pessoas por dia \n'
                   ' probabilidade de contaminação: {}% \n'
                   ' taxa Mortalidade: {}% '.format(contato, probabilidade * 100, mortalidade * 100))

        plt.ylabel('Habitantes')

        plt.plot(self.time, self.S, label='Susceptible', color='blue')
        plt.plot(self.time, self.I, label='Infected', color='orange')
        plt.plot(self.time, self.C, label='Mild symptoms', color='purple')
        # plt.plot(self.time, self.D, label='Precisando de Leitos', color='black')
        plt.plot(self.time, self.leitos, label='beds (5.623)', color='red')

        plt.legend()
        plt.grid()
        fig = plt.gcf()
        plt.show()
        fig.savefig('Curitiba_isolamento.png', format='png')


# Levando em conta os dados da COVID-19

c = 3  # contato entre as pessoas
p = 0.10  # probabilidade de contaminar
beta = c * p
tempo_de_contaminacao = 4  # o tempo de residência no compartimento infeccioso, isto é, o
# tempo médio em que um indivíduo pode infectar outras pessoas.
# Para a gripe, o período infecioso é tipicamente de 1 a 3 dias
gama = 1 / tempo_de_contaminacao  # coeficiente de recuperação.

mortalidade = 0.04


corona = Doenca(populacao=900000, beta=beta, gama=gama,
                tDeath=mortalidade, infectado=5100, simulationTime=360, leitos=5623)

corona.run()
corona.plot(mortalidade, c, p)
