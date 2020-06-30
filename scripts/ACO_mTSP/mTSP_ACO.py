#!/usr/bin/env python
#coding=utf-8

# ACO 演算 解決mTSP
# 預定跑9個點、共3隻螞蟻
# 原點、終點(0,0)

# create the graph
import createNodes
n=createNodes.nodenum()
nodes=createNodes.nodes()
edges=createNodes.edges()



# =================================================================================================================================================
# initialize  the parameters of the mTSP_ACO

import numpy as np
np.seterr(divide='ignore', invalid='ignore')
maxiter=400 # 最高迭帶次數
antNo=3 # 設定螞蟻數目
g_no=50 # 每次迭帶團數
tau0=10*1/(n*np.average(edges)) # 初始的pheromone
tau=tau0*np.ones((n,n)) # tau matrix
eta=1./edges # eta matrix 決定路徑的品質

rho=0.05 # 5% pheromone evaporates
alpha=2 # pheromone exponential parameters
beta=2  # desirability exponential parameters


groupindex=np.zeros((g_no,antNo)) # 製造出一個index以利讀取 為g_no列 antNo行
for x in range(g_no):
    for j in range(antNo):
        groupindex[x,j]=groupindex[x,j]+3*x+j

# main loop of the ACO
# =======================================================================================================================================================
bestFitness=float('inf')

for t in range(maxiter):
    import createTour
    tour=createTour.ctour(n,g_no,antNo,tau,eta,alpha,beta) # tour是由每次3組螞蟻組成的 總共有g_no團
    # print(tour) # 可以輸出tour行程

    # Calculate the fitness values of all ants
    # group_fitness 已更改為找出每次任務所需的最長距離
    group_fitness=[0]*g_no
    for i in range(g_no): # 旅團數 各旅團的fitness
        import m_fitnessFunction
        group_fitness[i]=group_fitness[i]+m_fitnessFunction.fit(i,tour,edges,g_no,antNo)

    # find the best tour
    # in order to find the minimum flight time

    minVal=min(group_fitness) # fitness中最小值
    minindex=group_fitness.index(minVal) # 回傳最小值index
    if minVal<bestFitness:
        bestFitness=group_fitness[minindex]
        bestTour=np.zeros((3,5))
        for i in range(3):
            for j in range(5):
                bestTour[i,j]=bestTour[i,j]+tour[int(groupindex[minindex,i]),j]

    # 從中再找到最佳的路徑解
    shortpath=float('inf') # 找出最小值
    group_index=0 # 初始group_index

    for i in range(g_no):
        if group_fitness[i]==bestFitness:
            import m_fitnessFunction
            totallen=m_fitnessFunction.totallen(i,tour,edges,g_no)

            if totallen<shortpath:
                shortpath=totallen # 找出最短總路徑
                index=i
                queen_tour=np.zeros((3,5))
                for x in range(3):
                    for j in range(5):
                        queen_tour[x,j]=queen_tour[x,j]+tour[int(groupindex[index,x]),j]


    queen_fitness=bestFitness

    # Update pherome matrix
    import m_updatePheromone
    tau= m_updatePheromone.up(g_no,n,tau,tour,edges)

    # evaporation
    tau=(1-rho)*tau

    # display the result
    # print('iteration #',t+1,'group length: ',queen_fitness)



import group_shortest
x=group_shortest.path_length(queen_tour,edges)

# print('最佳規畫路徑: \n')
# print('無人機1號路徑: ',queen_tour[0,:],' 1號路徑總長度為: ', x[0])
# print('無人機2號路徑: ',queen_tour[1,:],' 2號路徑總長度為: ', x[1])
# print('無人機3號路徑: ',queen_tour[2,:],' 3號路徑總長度為: ', x[2])

maximum=0
for i in range(3):
    if x[i]>maximum:
        maximum=x[i]
# print('此次任務最長執行距離(所需時間): ',maximum)


# import m_allplots # 繪製出結果
# m_allplots.btour(n,nodes,queen_tour,tau)

# ==========================================================================================================================================
# 輸出結果至 ros 執行 座標點
import coortran
a=coortran.tran(queen_tour[0,:],nodes)
xc0=a[:,0]
yc0=a[:,1]
b=coortran.tran(queen_tour[1,:],nodes)
xc1=b[:,0]
yc1=b[:,1]
c=coortran.tran(queen_tour[2,:],nodes)
xc2=c[:,0]
yc2=c[:,1]
print(a)
print("x0:",xc0); print("y0:",yc0)
print(b)
print("x1:",xc1); print("y1:",yc1)
print(c)
print("x2:",xc2); print("y2:",yc2)
#============================================================================================================================================
# building the talker node to send waypoints to commander_node
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from offb.msg import Floatsxyz
def talker():
    pub_0 = rospy.Publisher('/uav0/floats_0', Floatsxyz,queue_size=10)
    pub_1 = rospy.Publisher('/uav1/floats_1', Floatsxyz,queue_size=10)
    pub_2 = rospy.Publisher('/uav2/floats_2', Floatsxyz,queue_size=10)
    rospy.init_node('ACO_talker', anonymous=True)
    r = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        # a = np.array(wps.reshape(1,22), dtype=np.float32)
        # print(a)
        pub_0.publish(x=xc0, y=yc0)
        pub_1.publish(x=xc1, y=yc1)
        pub_2.publish(x=xc2, y=yc2)
        r.sleep()

if __name__ == '__main__':
    talker()
