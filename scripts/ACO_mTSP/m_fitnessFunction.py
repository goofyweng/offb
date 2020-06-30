#!/usr/bin/env python
#coding=utf-8
def fit(i,tour,edges,g_no,antNo):
    # i 會從 0 傳到 g_no
    # 找出所需最長距離
    fitness=[0]*3
    minifit=0
    import numpy as np
    groupindex=np.zeros((g_no,antNo)) # 製造出一個index以利讀取
    for x in range(g_no):
        for j in range(antNo):
            groupindex[x,j]=groupindex[x,j]+3*x+j

    for j in range(3):
        for x in range(4):

            currentNode=int(tour[int(groupindex[i,j]),x])
            nextNode=int(tour[int(groupindex[i,j]),x+1])

            fitness[j]=fitness[j]+edges[currentNode,nextNode]
    for j in range(3):
        if fitness[j]>minifit:
            minifit=fitness[j]

    return minifit

def totallen(i,tour,edges,g_no):
    # 找出所需最長距離的行程中 總路徑距離要最短
    # i 可以知道行程的編號 g_no
    import numpy as np

    total=0
    groupindex=np.zeros((g_no,3)) # 製造出一個index以利讀取

    for x in range(g_no):
        for j in range(3):
            groupindex[x,j]=groupindex[x,j]+3*x+j

    for j in range(3):
        for x in range(4):

            currentNode=int(tour[int(groupindex[i,j]),x])
            nextNode=int(tour[int(groupindex[i,j]),x+1])

            total=total+edges[currentNode,nextNode]

    return total
