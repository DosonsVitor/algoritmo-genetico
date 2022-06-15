'''
primeiro passo é criar uma população inicial de besouros
poderíamos usar valores booleanos, strings ou valores inteiros
para o nosso problema, irei utilizar valores inteiros de 0 a 255
'''
import csv
import numpy as np
from numpy.random import randint

populacao = []
numero_geracoes = 1000
tamanho_populacao = 100
fitness_populacao = []

def carregar_populacao():
  with open('besouros.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      besouro = [int(row[0]), int(row[1]), int(row[2])]
      populacao.append(besouro)

  return populacao

def fitness_function(x, index):
    return [x[0], x[1], x[2]], x[0] + x[1] + x[2], index

def avaliacao_fitness_populacao(populacao):
    for index in range(tamanho_populacao):
        fitness_populacao.append(fitness_function(populacao[index], index)[1])
    return fitness_populacao

def order(array):
    return array[0] + array[1] + array[2]

def selecao_ranking(populacao):
    populacao.sort(key=order)
    limite = int(len(populacao) / 2)
    selecao = populacao[0:limite]
    return selecao

def crossover(p1, p2):
    c1, c2 = p1.copy(), p2.copy()
    c1 = [p1[0], p2[1], p2[2]]
    c2 = [p2[0], p1[1], p1[2]]
    return [c1, c2]

def algoritmo_genetico():
    populacao = carregar_populacao()
    melhor_besouro, melhor_pontuacao, melhor_posicao = fitness_function(populacao[0], 0)
    for gen in range(numero_geracoes):
        fitness_populacao = avaliacao_fitness_populacao(populacao)
    
        # verifica o melhor besouro
        for i in range(tamanho_populacao):
            if fitness_populacao[i] < melhor_pontuacao:
                melhor_besouro, melhor_pontuacao, melhor_posicao = populacao[i], fitness_populacao[i], i
                #print(melhor_besouro, "É o melhor besouro, na posição %d, com pontuacao %d." % (melhor_posicao, melhor_pontuacao))

        selecionados = selecao_ranking(populacao)

        filhos = list()

        for i in range(0, tamanho_populacao, 2):
            p1, p2 = populacao[i], populacao[i+1]
            for filho in crossover(p1, p2):
                filhos.append(filho)

        populacao = selecionados
        
        selecionados = selecao_ranking(filhos)

        for i in selecionados:
            populacao.append(i)

        fitness_populacao.clear()

        
    print("Algoritmo Genético:")
    print(populacao)
    return [melhor_besouro, melhor_pontuacao]

melhor_besouro, melhor_pontuacao = algoritmo_genetico()
print('Melhor besouro: %s; Melhor pontuação: %d' % (melhor_besouro, melhor_pontuacao))