#!/usr/bin/env python
#coding=utf-8

# 輸出演算結果
def output1(queenTour,node):
    import numpy as np
    list1=[0]

    for i in range(10):
        if queenTour[0,i+1]!=queenTour[0,i]:
            list1.append(queenTour[0,i+1])

    n1=len(list1)
    coor1=np.zeros((n1,2))

    for k in range(n1):
        coor1[k,0]=coor1[k,0]+node[int(list1[k]),0]
        coor1[k,1]=coor1[k,1]+node[int(list1[k]),1]



    return coor1

def output2(queenTour,node):
    import numpy as np

    list2=[0]

    for i in range(10):

        if queenTour[1,i+1]!=queenTour[1,i]:
            list2.append(queenTour[1,i+1])
    n2=len(list2)
    coor2=np.zeros((n2,2))

    for k in range(n2):
        coor2[k,0]=coor2[k,0]+node[int(list2[k]),0]
        coor2[k,1]=coor2[k,1]+node[int(list2[k]),1]



    return coor2

def output3(queenTour,node):
    import numpy as np

    list3=[0]

    for i in range(10):

        if queenTour[2,i+1]!=queenTour[2,i]:
            list3.append(queenTour[2,i+1])

    n3=len(list3)
    coor3=np.zeros((n3,2))

    for k in range(n3):
        coor3[k,0]=coor3[k,0]+node[int(list3[k]),0]
        coor3[k,1]=coor3[k,1]+node[int(list3[k]),1]



    return coor3
