#!/usr/bin/env python
#coding=utf-8

# calculate the distance between each tours

import numpy as np
x = [0,19.47000,-6.47000,40.09000,5.39000,15.23000,-10,-20.47000,5.20000,16.30000]
y = [0,6.10000,-4.44000,-1.54000,6.37000,7.24000,4.05000,7.02000,7.666,-7.38000]

n=len(x) #計算點數

node=np.zeros((n,2)) # node 是2維矩陣

for i in range(n):
    node[i,0]=node[i,0]+x[i]
    node[i,1]=node[i,1]+y[i]

edges=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        x1=node[i,0]
        x2=node[j,0]
        y1=node[i,1]
        y2=node[j,1]

        edges[i,j]=edges[i,j]+((x2-x1)**2+(y2-y1)**2)**0.5

def nodenum():
    return n
def nodes():
    return node
def edgelen():
    return edges
