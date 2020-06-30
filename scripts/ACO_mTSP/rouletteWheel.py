#!/usr/bin/env python
#coding=utf-8
# 用來決定下一個該造訪的點
def choose(P):
    import random # 隨機模組
    import numpy as np
    n=len(P)
    P0=[0]*10
    for i in range(9):
        P0[i+1]=P0[i+1]+P[i]
    cumsumP=[0]*10
    # print('累積加成: \n',np.cumsum(P))
    cumsumP=cumsumP+np.cumsum(P0) # 累積總和
    # print(cumsumP)
    r=random.random() # 0~1之間的隨機亂數
    # print('產生的亂數為:',r)

    a=0
    for i in range(n):
        if r>=cumsumP[i]:
            a=a+1
    nextNode=a
    return nextNode
