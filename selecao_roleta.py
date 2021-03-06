import numpy as np
from numpy.random import randint

populacao = []
numero_geracoes = 10000
tamanho_populacao = 100
fitness_populacao = []

def gerar_populacao():
    return np.random.randint(255, size=(tamanho_populacao, 3))

def fitness_function(x, index):
    return [x[0], x[1], x[2]], x[0] + x[1] + x[2], index

def avaliacao_fitness_populacao(populacao):
    for index in range(tamanho_populacao):
        fitness_populacao.append(fitness_function(populacao[index], index)[1])
    return fitness_populacao

def selecao_roleta(populacao, fitness_populacao):
    soma = sum(fitness_populacao)
    proporcao = (fitness_populacao/soma) * 360

    proporcao_ind = []
    aux = 0
    selecionado = 0
    for i in range(tamanho_populacao):
        aux += proporcao[i]
        proporcao_ind.append(aux)
    lance = np.random.sample() * 360
    for i in range(tamanho_populacao):
        if(proporcao_ind[i] > lance):
            selecionado = populacao[i]
            break;
    return selecionado

def crossover(p1, p2):
    c1, c2 = p1.copy(), p2.copy()
    c1 = [p1[0], p2[1], p2[2]]
    c2 = [p2[0], p1[1], p1[2]]
    return [c1, c2]

def algoritmo_genetico():
    populacao = gerar_populacao()
    print(populacao)
    melhor_besouro, melhor_pontuacao, melhor_posicao = fitness_function(populacao[0], 0)
    for gen in range(numero_geracoes):
        fitness_populacao = avaliacao_fitness_populacao(populacao)
    
        # verifica o melhor besouro
        for i in range(tamanho_populacao):
            if fitness_populacao[i] < melhor_pontuacao:
                melhor_besouro, melhor_pontuacao, melhor_posicao = populacao[i], fitness_populacao[i], i
                print(melhor_besouro, "É o melhor besouro, na posição %d, com pontuacao %d." % (melhor_posicao, melhor_pontuacao))

        # selecionar os melhores da população e realizar nova geração
        selecionados = [selecao_roleta(populacao, fitness_populacao) for _ in range(tamanho_populacao)]

        filhos = list()

        for i in range(0, tamanho_populacao, 2):
            p1, p2 = selecionados[i], selecionados[i+1]
            for filho in crossover(p1, p2):
                filhos.append(filho)
        populacao = filhos
    print("Algoritmo Genético:")
    print(populacao)
    return [melhor_besouro, melhor_pontuacao]

melhor_besouro, melhor_pontuacao = algoritmo_genetico()
print('Melhor besouro: %s; Melhor pontuação: %d' % (melhor_besouro, melhor_pontuacao))