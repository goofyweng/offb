#!/usr/bin/env python
#coding=utf-8
# 使用於轉換旅行點 成為座標點
def tran(tour,nodes):
    # tour會是一個1維矩陣 共有五個元素
    import numpy as np
    coor=np.zeros((5,2))

    for i in range(5):
        for j in range(2):
            coor[i,j]=coor[i,j]+nodes[int(tour[i]),j]

    return coor
