#!/usr/bin/env python
#coding=utf-8

# update pheromone matrix
def updatePheromone(tau,colony,gp,n,antNo,edges):

    for i in range(antNo):
        for j in range(gp):
            for k in range(n):

                currentNode=int(colony[int(3*i+j),k])
                nextNode=int(colony[int(3*i+j),k+1])

                import f
                groupfitness=f.group_len(i,j,n,colony,edges,antNo) # 每旅行團總長

                tau[currentNode,nextNode]=tau[currentNode,nextNode]+1/groupfitness
                tau[nextNode,currentNode]=tau[nextNode,currentNode]+1/groupfitness

    return (tau)
