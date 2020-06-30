#!/usr/bin/env python
#coding=utf-8
# 假設所有無人機的速度皆一樣、則組內的最長飛時就是本次任務所需的最短時間
# 每組內會有三架無人機出任務
def path_length(queen_tour,edges):

    import numpy as np
    fitness=[0]*3

    for j in range(3):
        for x in range(4):

            currentNode=int(queen_tour[j,x])
            nextNode=int(queen_tour[j,x+1])
            fitness[j]=fitness[j]+edges[currentNode,nextNode]


    return fitness

def indi_path(inditour,edges):
    import numpy as np
    fitness=[0]

    for x in range(4):

        currentNode=int(inditour[x])
        nextNode=int(inditour[x+1])
        fitness[0]=fitness[0]+edges[currentNode,nextNode]
    return fitness
