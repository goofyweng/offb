#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib
import matplotlib.pyplot as plt # 為了繪製出圖形

# 繪製出圖片 以best tour為第一優先
def btour(n,node,queenTour):
    fig, ax=plt.subplots(1,3,figsize=(10,12)) # 想要有3張圖
    mngr = plt.get_current_fig_manager()  # 获取当前figure manager
    mngr.window.wm_geometry("+200+5")  # 调整窗口在屏幕上弹出的位置


    x=[0]*n
    y=[0]*n
    for i in range(n):
        x[i]=x[i]+node[i,0]
        y[i]=y[i]+node[i,1]

    # 繪製出第一張圖片 all nodes=======================================================================================================================
    ax[0].scatter(x,y)
    ax[0].set_title('All nodes')


    for i in range(n):
        ax[0].text(x[i]+0.5,y[i]+0.5,i,fontsize=15,verticalalignment="top",horizontalalignment="right")



    # 繪製出第二張圖 all possible route ==================================================================================================================
    for i in range(n-1):

        for j in range(n-1):

            x1=x[i]
            y1=y[i]
            x2=x[j+1]
            y2=y[j+1]
            X=[x1,x2]
            Y=[y1,y2]
            ax[1].plot(X,Y,'k',linewidth=2,marker='o',markerfacecolor='blue',markeredgecolor='orange',markersize=10,markeredgewidth=1.5)

    ax[1].set_title('All possible route')

    # 繪製出第三張圖 queen tour==========================================================================================================================


    qx=[0]*(n+1)
    qy=[0]*(n+1)



    for i in range(n+1): # queen tour的轉換

        qx[i]=qx[i]+x[int(queenTour[0,i])]
        qy[i]=qy[i]+y[int(queenTour[0,i])]


    ax[2].plot(qx,qy,'b',linewidth=2,marker='o',markerfacecolor='blue',markeredgecolor='orange',markersize=10,markeredgewidth=1.5)

    qx=[0]*(n+1)
    qy=[0]*(n+1)

    for i in range(n+1): # queen tour的轉換

        qx[i]=qx[i]+x[int(queenTour[1,i])]
        qy[i]=qy[i]+y[int(queenTour[1,i])]

    ax[2].plot(qx,qy,'r',linewidth=2,marker='o',markerfacecolor='blue',markeredgecolor='orange',markersize=10,markeredgewidth=1.5)

    qx=[0]*(n+1)
    qy=[0]*(n+1)

    for i in range(n+1): # queen tour的轉換

        qx[i]=qx[i]+x[int(queenTour[2,i])]
        qy[i]=qy[i]+y[int(queenTour[2,i])]

    ax[2].plot(qx,qy,'g',linewidth=2,marker='o',markerfacecolor='blue',markeredgecolor='orange',markersize=10,markeredgewidth=1.5)
    ax[2].set_title('Queen Tour')

    # plt.ioff() # 關閉互動模式
    plt.show()
