#!/usr/bin/env python
#coding=utf-8
def up(antNo,n,tau,tour,ant_fitness):


    for i in range(antNo):
        for j in range(n-1):
            currentNode=int(tour[i,j])
            nextNode=int(tour[i,j+1])

            tau[currentNode,nextNode]=tau[currentNode,nextNode]+1/ant_fitness[i]
            tau[nextNode,currentNode]=tau[nextNode,currentNode]+1/ant_fitness[i]


    return tau
