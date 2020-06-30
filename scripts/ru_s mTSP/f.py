#!/usr/bin/env python
#coding=utf-8

# calculate the individual ant's fitness
def longest_len(colony,edges,antNo,gp,n):
    # 回傳本次旅行團所需的最長距離
    import numpy as np

    indi_max=np.zeros((antNo,1))


    for i in range(antNo):
        length=np.zeros((gp,1))

        for k in range(gp):
            for j in range(n):
                # n=10, j=0~9
                currentNode=int(colony[int(3*i+k),j])
                nextNode=int(colony[int(3*i+k),j+1])

                length[k,0]=length[k,0]+edges[currentNode,nextNode]
        maxi=0
        for t in range(3):
            if length[t,0]>maxi:
                maxi=length[t,0]



        indi_max[i,0]=indi_max[i,0]+maxi

    return (indi_max)

# calculate total length
def total_len(i,colony,edges,antNo,gp,n):
    # 計算個別旅團total len
    # i 代表第幾團
    total=0
    for k in range(gp):
        for x in range(n):
            # n=10, x=0~9
            currentNode=int(colony[int(3*i+k),x])
            nextNode=int(colony[int(3*i+k),x+1])

            total=total+edges[currentNode,nextNode]
    return (total)

def group_len(i,j,n,colony,edges,antNo):
    # 最小單位的總長度
    # i 為antNo j為第幾團 n為點數
    total=0


    for k in range(n):
        currentNode=int(colony[int(3*i+j),k])
        nextNode=int(colony[int(3*i+j),k+1])

        total=total+edges[currentNode,nextNode]

    return (total)

def total(bestTour,edges,gp,n):
    # 專門為bestTour 找到最短總路徑
    tolen=0
    for i in range(gp):
        for j in range(n):

            currentNode=int(bestTour[i,j])
            nextNode=int(bestTour[i,j+1])

            tolen=tolen+edges[currentNode,nextNode]
    return(tolen)
