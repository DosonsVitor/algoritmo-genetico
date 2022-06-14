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

def selecao(populacao, fitness_populacao, k=3):
    # primeira seleção aleatória por torneio
    selecao_ix = randint(0, len(populacao))
    for ix in randint(0, len(populacao), k-1):
        if fitness_populacao[ix] < fitness_populacao[selecao_ix]:
            selecao_ix = ix
    return populacao[selecao_ix]

def crossover(p1, p2):
    c1, c2 = p1.copy(), p2.copy()
    c1 = [p1[0], p2[1], p2[2]]
    c2 = [p2[0], p1[1], p1[2]]
    return [c1, c2]


#Mutação em 1% do individuos aleatorios da população
def mutacao(populacao):
    numero_mutacoes = int(tamanho_populacao * 0.01)
    besouros_mutados = []
    for i in range(numero_mutacoes):
        index_mutacao = randint(0, tamanho_populacao)
        while(index_mutacao in besouros_mutados):
            index_mutacao = randint(0, tamanho_populacao)

        besouros_mutados.append(index_mutacao)
        populacao[index_mutacao][1] += 50
        if(populacao[index_mutacao][1] > 255):
            populacao[index_mutacao][1] = 255
    
    return populacao

def algoritmo_genetico():
    populacao = mutacao(gerar_populacao())
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
        selecionados = [selecao(populacao, fitness_populacao) for _ in range(tamanho_populacao)]

        filhos = list()

        for i in range(0, tamanho_populacao, 2):
            p1, p2 = selecionados[i], selecionados[i+1]
            for filho in crossover(p1, p2):
                filhos.append(filho)
        populacao = mutacao(filhos)
    print("Algoritmo Genético:")
    print(populacao)
    return [melhor_besouro, melhor_pontuacao]

melhor_besouro, melhor_pontuacao = algoritmo_genetico()
print('Melhor besouro: %s; Melhor pontuação: %d' % (melhor_besouro, melhor_pontuacao))