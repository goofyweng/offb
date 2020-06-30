#!/usr/bin/env python
#coding=utf-8
# 獨立決定出三隻螞蟻的行程
import random
import numpy as np

#================================================================================================================
def possibility(n,g_no,antNo,tau,eta,alpha,beta):
    ant_tours=np.zeros((3,5))

    # 選取初次造訪點===================================================================================================
    listnode=[1,2,3,4,5,6,7,8,9]
    # 選取經過點
    # 依序選擇初次造訪點
    initial_node=random.sample(listnode,3) # 會是一個list

    ant_tours[0,1]=ant_tours[0,1]+initial_node[0]
    ant_tours[1,1]=ant_tours[1,1]+initial_node[1]
    ant_tours[2,1]=ant_tours[2,1]+initial_node[2]

    P_allNodes=[1]*(n-1)  # 全為1的矩陣 機率 一維 第一隻螞蟻可以選6個造訪點 分別代表1~9 n=10
    P_allNodes[int(ant_tours[0,1])-1]=0
    P_allNodes[int(ant_tours[1,1])-1]=0
    P_allNodes[int(ant_tours[2,1])-1]=0


    for i in range(2):
        for j in range(3):
            currentNode=int(ant_tours[j,i+1]) # 不會有0
            sumP=0
            for t in range(n-1):
                if P_allNodes[t]!=0:
                    P_allNodes[t]=(tau[currentNode,t+1]**alpha)*(eta[currentNode,t+1]**beta) # tau 是10*10的矩陣
                sumP=sumP+P_allNodes[t]
            P=P_allNodes/sumP

            import rouletteWheel
            nextNode=rouletteWheel.choose(P)
            ant_tours[j,i+2]=ant_tours[j,i+2]+nextNode
            P_allNodes[nextNode-1]=0

    return ant_tours
