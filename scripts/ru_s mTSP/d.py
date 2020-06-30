#!/usr/bin/env python
#coding=utf-8

# create ants

def createTour(edges,eta,tau,alpha,beta,lamda,gp,antNo):
    import numpy as np
    import random

    nodeNo=10
    alpha0=2
    beta0=2
    lambda0=1
    kappa=[0]*nodeNo # 設定kappa初始值
    tour=np.zeros((gp*antNo,nodeNo+1)) # 所有旅行團的矩陣

    for x in range(antNo):
        group=[0,1,2]
        gpgo=random.sample(group,1) # 決定初次可以動作的旅團 gpgo是list

        # tour[3*0+gpgo,0]=initial_node # 0可以替換成k

        P_allNodes=[1]*(nodeNo)  # 全為1的矩陣 機率 一維 共10點 0為第一點
        P_allNodes[0]=0 # 將原點的機率設為0 不再經過原點

        for i in range(nodeNo-1):
            # nodeNo-1=9 也就是0-8 共有9次

            currentNode=int(tour[int(3*x+gpgo[0]),i]) # gpgo是list

            for k in range(nodeNo):
                # kappa 為1*10的矩陣
                kappa[k]=kappa[k]+alpha0*edges[currentNode,0]+beta0*edges[0,k]-lambda0*edges[currentNode,k]

            P_allNodes[currentNode]=0 # 走過的路線機率變為0
            sumP=0 # sumP需要歸零

            for t in range(nodeNo): # 0~9
                if P_allNodes[t]!=0:
                    P_allNodes[t]=(tau[currentNode,t]**alpha)*(eta[currentNode,t]**beta)*(kappa[t]**lamda)
                sumP=sumP+P_allNodes[t]

            P=P_allNodes/sumP

            import e
            nextNode=e.choose(P) #決定出下一個node rouletteWheel
            tour[int(3*x+gpgo[0]),i+1]=tour[int(3*x+gpgo[0]),i+1]+nextNode # 更新下一個點

            P_allNodes[nextNode]=0 # 走過的路線機率變為0

            group.remove(gpgo[0]) # 刪除掉指定元素
            # 未被選中的旅團就只能待在原點
            tour[int(3*x+group[0]),i+1]=tour[int(3*x+group[0]),i+1]+tour[int(3*x+group[0]),i] # 更新下一個點
            tour[int(3*x+group[1]),i+1]=tour[int(3*x+group[1]),i+1]+tour[int(3*x+group[1]),i] # 更新下一個點

            group=[0,1,2]
            gpgo=random.sample(group,1) # 決定每次可以動作的旅團

    return (tour)
