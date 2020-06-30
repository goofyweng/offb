#!/usr/bin/env python
#coding=utf-8
# 收到queen tour之後 回傳座標點
def coordinates(queen_tour,nodes):
    # nodes 點 從0至末點
    # queen tour為單維 list
    # 因為有9個點 總共應該有11排
    import numpy as np
    coord=np.zeros((11,2))

    for i in range(11):
        coord[i,0]=coord[i,0]+nodes[int(queen_tour[i]),0]
        coord[i,1]=coord[i,1]+nodes[int(queen_tour[i]),1]

    return coord
