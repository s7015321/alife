#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, InputLayer
from alifebook_lib.simulators import AntSimulator
from ant_nn_utils_d1 import generate_nn_model, generate_action, decode_weights, get_gene_length, CONTEXT_NEURON_NUM

# GAに関するパラメタ
ONE_TRIAL_STEP = 0
POPULATION_SIZE = 51
TIME_STEP=0

nn_model = generate_nn_model()

GENE_LENGTH = get_gene_length(nn_model)
population = np.random.random((POPULATION_SIZE, GENE_LENGTH)) * 10 - 5
offsprings = np.empty(population.shape)
fitness = np.empty(POPULATION_SIZE)
stamina = np.empty(POPULATION_SIZE)


def select(population, fitness, TOURNAMENT_SIZE = 3):
    idxs = np.random.choice(range(len(population)), TOURNAMENT_SIZE, replace=False)
    fits = fitness[idxs]
    winner_idx = idxs[np.argmax(fits)]
    return population[winner_idx]


simulator = AntSimulator(1)
generation = 0
while True:

    # 現在の集団を評価する
    for gene_index, gene in enumerate(population):
        print('.', end='', flush=True)
        # 遺伝子情報をニューラルネットワークの重みにデコードする
        decode_weights(nn_model, gene)
        # シミュレーション実行
        context_val = np.zeros(CONTEXT_NEURON_NUM)
        simulator.reset()
        ONE_TRIAL_STEP=0
        TIME_STEP=0
        while ONE_TRIAL_STEP<2000:
            sensor_datas = simulator.get_sensor_data()
            action, context_val = generate_action(nn_model, sensor_datas[0], context_val)
            simulator.update(action)
            if action[:,0]>0.8:
                ONE_TRIAL_STEP+=4
                TIME_STEP+=1
            elif 0.5<action[:,0]<=0.8:
                ONE_TRIAL_STEP+=3
                TIME_STEP+=1    
            elif 0.3<action[:,0]<=0.5:
                ONE_TRIAL_STEP+=2
                TIME_STEP+=1
            elif action[:,0]<=0.3:
                ONE_TRIAL_STEP+=1
                TIME_STEP+=1
      
    
        # 今回のフィットネスを保存
        fitness[gene_index] = simulator.get_fitness()[0]
        stamina[gene_index] = TIME_STEP

    # 結果をレポート
    print()
    print("generation:", generation)
    print("fitness mean:", np.mean(fitness),"stamina mean:",np.mean(stamina)) 
    print("         std:", np.std(fitness), "         std:",np.std(stamina))
    print("         max:", np.max(fitness), "         max:",stamina[np.argmax(fitness)])
    print("         min:", np.min(fitness), "         min:",stamina[np.argmin(fitness)])
    
    # １位のエージェントはファイルに保存
    best_idx = np.argmax(fitness)
    best_individual = population[best_idx]
    np.save("gen{0:04}_best.npy".format(generation), best_individual)

    # １位のエージェントはそのまま次世代に
    offsprings[0] = best_individual.copy()

    # POPULATION_SIZE/3 - 1匹は次世代にコピーされる
    for i in range(1, POPULATION_SIZE//3):
        offspring = select(population, fitness).copy()
        offsprings[i] = offspring

    # POPULATION_SIZE/3匹は突然変異後に次世代に
    for i in range(POPULATION_SIZE//3, 2*POPULATION_SIZE//3):
        offspring = select(population, fitness).copy()
        mut_idx = np.random.randint(GENE_LENGTH)
        offspring[mut_idx] += np.random.randn()
        offsprings[i] = offspring

    # POPULATION_SIZE/3匹は交叉後に次世代に
    for i in range(2*POPULATION_SIZE//3, POPULATION_SIZE, 2):
        p1 = select(population, fitness).copy()
        p2 = select(population, fitness).copy()
        xo_idx = np.random.randint(1, GENE_LENGTH)
        offspring1 = np.r_[p1[:xo_idx], p2[xo_idx:]]
        offspring2 = np.r_[p2[:xo_idx], p1[xo_idx:]]
        offsprings[i] = offspring1
        try:
            offsprings[i+1] = offspring2
        except IndexError:
            pass  # pupulationがいっぱいの時は破棄

    population = offsprings.copy()

    generation += 1
