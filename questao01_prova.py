'''
primeiro passo é criar uma população inicial de besouros
poderíamos usar valores booleanos, strings ou valores inteiros
para o nosso problema, irei utilizar valores inteiros de 0 a 255
'''
import csv
import numpy as np
from numpy.random import randint

populacao = []
numero_geracoes = 10000
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
    populacao = carregar_populacao()
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
        fitness_populacao.clear()
   
    return [melhor_besouro, melhor_pontuacao]

def organizar(array):
    return { 'Besouro': [array[0][0], array[0][1], array[0][2]], 'Pontuacao': array[1]}

def media(array):
    soma = 0
    for i in range(len(array)):
        soma += array[i]['Pontuacao']
    return soma / len(array)

melhores = []

for i in range(3):
    melhores.append(organizar(algoritmo_genetico()))
    populacao = []
    fitness_populacao = []
print('Melhores besouros: ')
print(melhores)
print('Media:')
print(media(melhores))