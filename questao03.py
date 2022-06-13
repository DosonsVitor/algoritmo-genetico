from ast import For
import numpy as np
from numpy.random import randint

populacao = []
numero_geracoes = 300
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

def algoritmo_genetico():
    populacao = gerar_populacao()
    melhor_besouro, melhor_pontuacao, melhor_posicao = fitness_function(populacao[0], 0)
    for gen in range(numero_geracoes):
        fitness_populacao = avaliacao_fitness_populacao(populacao)
    
        # verifica o melhor besouro
        for i in range(tamanho_populacao):
            if fitness_populacao[i] < melhor_pontuacao:
                melhor_besouro, melhor_pontuacao, melhor_posicao = populacao[i], fitness_populacao[i], i

        # selecionar os melhores da população e realizar nova geração
        selecionados = [selecao(populacao, fitness_populacao) for _ in range(tamanho_populacao)]

        filhos = list()

        for i in range(0, tamanho_populacao, 2):
            p1, p2 = selecionados[i], selecionados[i+1]
            for filho in crossover(p1, p2):
                filhos.append(filho)
        populacao = filhos
    return [melhor_besouro, melhor_pontuacao]

def organizar(array):
    return { 'Besouro': [array[0][0], array[0][1], array[0][2]], 'Pontuacao': array[1]}

def media(array):
    soma = 0
    for i in range(len(array)):
        soma += array[i]['Pontuacao']
    return soma / len(array)

melhores = [[],[],[]]

for i in range(3):
    for j in range(5):
        melhores[i].append(organizar(algoritmo_genetico()))
        fitness_populacao = []
    print('Melhores besouros em 5 repeticoes de %d geracoes: ' % numero_geracoes)
    print(melhores[i])
    print('Media:')
    print(media(melhores[i]))
    numero_geracoes *= 2




#print(melhores)
# melhor_besouro, melhor_pontuacao = algoritmo_genetico()
# print('Melhor besouro: %s; Melhor pontuação: %d' % (melhor_besouro, melhor_pontuacao))