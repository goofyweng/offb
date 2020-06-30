#!/usr/bin/env python
#coding=utf-8

# ruru's aco algorithm
# to solve the mtsp problem
# with 9 points to visit & 3 drones
#=====================================================================================================================================

#  ACO algorithm
#====================================================================================================================================
# graph data
import b
import numpy as np
n=b.nodenum() #得知點數 會有10個點
node=b.nodes() #2維矩陣 第一行為x 第二行為y
edges=b.edgelen() #各邊的長度 10*10維度
#=====================================================================================================================================
# initialize parameters

maxiter=300
antNo=20
gp=3

np.seterr(divide='ignore', invalid='ignore')
tau0=10*1/(n*np.mean(edges))   # Initial pheromone concentration
tau=tau0*np.ones((n,n)) # Pheromone matirx
eta=1/edges  # desirability of each edge

rho=0.15 # Evaporation rate
alpha=1  # Pheromone exponential parameters
beta=3  # Desirability exponetial paramter
lamda=2

#=====================================================================================================================================
# main loop of ACO

bestFitness=float('inf')
maxiFitness=float('inf')
bestTour=np.zeros((gp,n+1))
queenTour=np.zeros((gp,n+1))

for t in range(maxiter):

    # create ants
    import d
    colony=d.createTour(edges,eta,tau,alpha,beta,lamda,gp,antNo) # colony 是一個 30*11的矩陣 第一團為1-3排...

    # calculate the individual ant's fitness & total fitness
    # indivioual fitness 需要傳回此旅行團的最遠值 為了 minimum longest distance
    import f
    indi_max=f.longest_len(colony,edges,antNo,gp,n)
    # print(indi_max)

    # find minimum longest length

    for i in range(antNo):
        if indi_max[i,0]<bestFitness:
            bestFitness=indi_max[i,0]
            bestindex=i
            for k in range(gp):
                for x in range(n+1):

                    bestTour[k,x]=colony[int(3*bestindex+k),x]

    for i in range(antNo):
        if indi_max[i,0]==bestFitness:
            import f
            totallen=f.total(bestTour,edges,gp,n)
            if totallen<maxiFitness:
                maxiFitness=totallen
                queenTour=bestTour

    # update pheromone matrix
    import g
    tau=g.updatePheromone(tau,colony,gp,n,antNo,edges)

    # evaporation
    tau=(1-rho)*tau

    # display the result
    # print('iteration #',t+1,'best fitness: ',bestFitness, 'minimum total len: ',maxiFitness)

# print('iteration #',t+1,'best fitness: ',bestFitness, 'minimum total len: ',maxiFitness)
# print(queenTour)

#==================================================================================================
# 顯示結果
import i
coord1=i.output1(queenTour,node)
coord2=i.output2(queenTour,node)
coord3=i.output3(queenTour,node)

xc0=coord1[:,0]
yc0=coord1[:,1]
xc1=coord2[:,0]
yc1=coord2[:,1]
xc2=coord3[:,0]
yc2=coord3[:,1]

print(coord1)
print("x0:",xc0); print("y0:",yc0)
print(coord2)
print("x1:",xc1); print("y1:",yc1)
print(coord3)
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
# endresult=np.zeros((15,2))
# coord1_dim=coord1.shape
# coord2_dim=coord2.shape
# coord3_dim=coord3.shape
#
#
# for i in range(coord1.shape[0]):
#     for k in range(2):
#         endresult[i,k]=endresult[i,k]+coord1[i,k]
#
# for i in range(coord2.shape[0]):
#     for k in range(2):
#         endresult[int(coord1.shape[0]+i),k]=endresult[int(coord1.shape[0]+i),k]+coord2[i,k]
#
# for i in range(coord3.shape[0]):
#     for k in range(2):
#         endresult[int(coord1.shape[0]+coord2.shape[0]+i),k]=endresult[int(coord1.shape[0]+coord2.shape[0]+i),k]+coord3[i,k]

# print(endresult) # endresult為一個大矩陣 15*2
# import h # 繪製出結果
# h.btour(n,node,queenTour)
