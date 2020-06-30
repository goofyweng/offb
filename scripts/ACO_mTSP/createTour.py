#!/usr/bin/env python
#coding=utf-8
# create tour for mTSP

def ctour(n,g_no,antNo,tau,eta,alpha,beta):
    # g_no 為單次迭帶旅團數
    import random # 隨機模組
    import numpy as np

    tour=np.zeros((antNo*g_no,5))

    groupindex=np.zeros((g_no,antNo)) # 製造出一個index以利讀取
    for i in range(g_no):
        for j in range(antNo):
            groupindex[i,j]=groupindex[i,j]+3*i+j


    # 為了整合進入tour matrix (是一個30*5的矩陣)
    for i in range(g_no):
        import antTour
        anttours=antTour.possibility(n,g_no,antNo,tau,eta,alpha,beta)
        for j in range(antNo):
            for k in range(5):
                tour[int(groupindex[i,j]),k]=tour[int(groupindex[i,j]),k]+anttours[j,k]
    return tour
