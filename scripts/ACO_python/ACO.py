#!/usr/bin/env python
#coding=utf-8
# ACO 演算
# import rospy
# create the graph
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import createGraph
n=createGraph.nodenum()
nodes=createGraph.nodes()
edges=createGraph.edges()
# createGraph.plot()  # 繪製出圖型
# print('node的數目: ', n)
# print('選擇的點: \n' , nodes)
# print('各點間距離的矩陣: \n',edges)

# =================================================================================================================================================
# initialize  the parameters of the ACO

import numpy as np
np.seterr(divide='ignore', invalid='ignore')
maxiter=200 # 最高迭帶次數
antNo=30 # 設定螞蟻數目
tau0=10*1/(n*np.average(edges)) # 初始的pheromone
tau=tau0*np.ones((n,n)) # tau matrix
eta=1./edges # eta matrix 決定路徑的品質

rho=0.05 # 5% pheromone evaporates
alpha=1 # pheromone exponential parameters
beta=1  # desirability exponential parameters

# main loop of the ACO
# =======================================================================================================================================================
bestFitness=float('inf')
# bestTour=[] # 有序可更動列表 list
# 產生list 0,1,2...99 共會執行maxiter次
for t in range(maxiter):
    import createColony
    tour=createColony.colony(n,antNo,tau,eta,alpha,beta)
    # 可以輸出tour 行程

    # Calculate the fitness values of all ants
    ant_fitness=[0]*antNo
    for i in range(antNo):
        import fitnessFunction
        ant_fitness[i]=ant_fitness[i]+fitnessFunction.fit(tour[i,:],edges)

    # find the best ant(queen)
    minVal=min(ant_fitness) # fitness中最小值
    minindex=ant_fitness.index(minVal) # 回傳最小值index
    if minVal<bestFitness:
        bestFitness=ant_fitness[minindex]
        bestTour=tour[minindex,:]

    queen_tour=bestTour
    queen_fitness=bestFitness

    # Update pherome matrix
    import updatePherome
    tau = updatePherome.up(antNo,n,tau,tour,ant_fitness)

    # evaporation
    tau=(1-rho)*tau

    # display the result
    # print('iteration #',t+1,'shortest length: ',queen_fitness)



# print('最佳規畫路徑: \n',queen_tour)

# 輸出座標點
import export_coord
wps=export_coord.coordinates(queen_tour,nodes)
# wps.dtype.name = float64
xc=wps[:,0]
yc=wps[:,1]
print(wps)
print(xc)
print(yc)
# print(type(export_coord.coordinates(queen_tour,nodes)))
#class 'numpy.ndarray'

# import allplots # 繪製出結果
# allplots.btour(n,nodes,queen_tour)

# arr =export_coord.coordinates(queen_tour,nodes)
# ts = arr.tostring()
# print np.fromstring(ts,dtype=float)
# print(type(np.fromstring(ts,dtype=float)))
# import rospy
# from std_msgs.msg import Float64MultiArray
#=================================================================================
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from offb.msg import Floatsxyz
def talker():
    pub = rospy.Publisher('floats', Floatsxyz,queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        # a = np.array(wps.reshape(1,22), dtype=np.float32)
        # print(a)
        pub.publish(x=xc, y=yc)
        r.sleep()

if __name__ == '__main__':
    talker()
