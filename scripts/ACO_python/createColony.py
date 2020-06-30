#!/usr/bin/env python
#coding=utf-8
def colony(n,antNo,tau,eta,alpha,beta):
    import random # 隨機模組
    import numpy as np
    import rouletteWheel
    np.seterr(divide='ignore', invalid='ignore')
    tour=np.zeros((antNo,n+1)) # 11個點 決定第1~第9點的點

    for i in range(antNo):
        listnode=[1,2,3,4,5,6,7,8,9]
        initial_node=random.sample(listnode,1) # 隨機選取初次造訪點
        tour[i,1]=int(tour[i,1]+initial_node[0]) # 初始的node值
        P_allNodes=[1]*(n)  # 全為1的矩陣 機率 一維 共10點 0為第一點
        P_allNodes[0]=0 # 將原點的機率設為0 不再經過原點

        for j in range(n-2): # 0~7

            currentNode=int(tour[i,j+1]) # node是整數
            P_allNodes[currentNode]=0 # 走過的路線機率變為0
            sumP=0
            for t in range(n): # 0~9
                if P_allNodes[t]!=0:
                    P_allNodes[t]=(tau[currentNode,t]**alpha)*(eta[currentNode,t]**beta)
                # else:
                #     P_allNodes[0,t]=0
                sumP=sumP+P_allNodes[t]

            P=P_allNodes/sumP # 依然是一個list
            # print('目前各節點的機率: \n',P)
            nextNode=rouletteWheel.choose(P) #決定出下一個node
            # print('=======================================================================')
            # print('下一個節點: \n',nextNode)
            # print('=======================================================================')
            tour[i,j+2]=nextNode
            # print('目前的行程: \n',tour)
            # print('=======================================================================')
        # 將迴路完整
        tour[i,j+3]=tour[i,j+3]+tour[i,0] # 回到最一開始的點
    return tour
