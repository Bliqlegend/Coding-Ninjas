#!/usr/bin/env python
# coding: utf-8

# In[17]:


import queue

class Graph:
    def __init__(self,n,ne):
        self.n = n
        self.ne = ne
        self.adjMatrix = [[0 for j in range(n)] for i in range(n)]
    
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] =1
        self.adjMatrix[v2][v1] = 1
    
    def cel(self,v):
        arr = []
        for i in range(self.n):
            if self.adjMatrix[v][i] == 1:
                arr.append(i)
        return arr
                
    
    def bfs(self):
        q = queue.Queue()
        q.put(0)
        visited = [False for i in range(self.n)]
        visited[0] = True
        while q.empty() is False:
            u = q.get()
            print(u,end=' ')
            for i in range(self.ne):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
    
    def containsEdge(self,v1,v2):
        print("printing v1 v2")
        print(v1,end=' ')
        print(v2,end=' ')

        if self.adjMatrix[v1][v2] > 0:
            return True
        return False
    
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v2] = 0
        
    def __str__(self):
        return str(self.adjMatrix)

def takeInput():
    ele = []
    ele = [int(element) for element in list(input().strip().split(" "))]
    nv = ele[0]
    ne = ele[1]
    arr = [[0 for i in range(ne)] for i in range(ne)]
    idx = 0
    ele = []
    for i in range(ne):
        if idx > ne-1:
            break
        ele = [int(element) for element in list(input().strip().split(" "))]
        arr[idx] = ele
        idx+=1
    return nv,ne,arr


# nv,ne,arr = takeInput()
# g = Graph(nv,ne)
# i= 0
# j= 0
# while i < nv and j < ne:
#     g.addEdge(arr[i][0],arr[i][1])
#     i+=1
#     j+=1
# g.bfs()

