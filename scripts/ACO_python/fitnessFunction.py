#!/usr/bin/env python
#coding=utf-8
def fit(tour,edges):
    fitness=0
    for i in range(len(tour)-1):

        currentNode=int(tour[i])
        nextNode=int(tour[i+1])

        fitness=fitness+edges[currentNode,nextNode]
    return fitness
