#!/usr/bin/env python
#coding=utf-8
# 輸入點 並且 計算 各自的距離
import numpy as np

# 原點+9 個節點 原點設為index 0
x = [0,19.47000,-6.47000,40.09000,5.39000,15.23000,-10,-20.47000,5.20000,16.30000]
y = [0,6.10000,-4.44000,-1.54000,6.37000,7.24000,4.05000,7.02000,7.666,-7.38000]


# ====================================================================================================================================
n=len(x) # 知道總共有幾個點
node=np.zeros((n,2)) # node 是2維矩陣

for i in range(n):
    node[i,0]=node[i,0]+x[i]
    node[i,1]=node[i,1]+y[i]
# print('點的座標: \n', node)

edge=np.zeros((n,n)) # 創造點跟點的距離矩陣
for i in range(n):
    for j in range(n):
        x1=node[i,0]
        x2=node[j,0]
        y1=node[i,1]
        y2=node[j,1]
        edge[i,j]=((x1-x2)**2+(y1-y2)**2)**0.5



def nodenum():
    return n

def nodes():
    return node

def edges():
    return edge
