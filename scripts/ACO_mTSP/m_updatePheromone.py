#!/usr/bin/env python
#coding=utf-8
def up(g_no,n,tau,tour,edges):
    import numpy as np

    groupindex=np.zeros((g_no,3)) # 製造出一個index以利讀取 為g_no列 antNo行
    for x in range(g_no):
        for j in range(3):
            groupindex[x,j]=groupindex[x,j]+3*x+j




    for i in range(g_no):
        for j in range(3):
            import group_shortest
            fitness=group_shortest.indi_path(tour[int(groupindex[i,j]),:],edges)

            for k in range(4):
                currentNode=int(tour[int(groupindex[i,j]),k])
                nextNode=int(tour[int(groupindex[i,j]),k+1])
            # print('===============================',fitness)

                tau[currentNode,nextNode]=tau[currentNode,nextNode]+1/fitness[0]
                tau[nextNode,currentNode]=tau[nextNode,currentNode]+1/fitness[0]



    return tau
