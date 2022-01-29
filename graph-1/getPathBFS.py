from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

import queue

class Graph:
    def __init__(self,n,ne):
        self.n = n
        self.ne = ne
        self.adjMatrix = [[0 for j in range(n)] for i in range(n)]
    
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def containsEdge(self,v1,v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        return False
    
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v2] = 0

    def getPathBFSHelper(self,vf,vs,visited):
        mapp = {}
        q = queue.Queue()
        
        if self.adjMatrix[vf][vs] == 1 and vf == vs:
            ans = []
            ans.append(vf)
            return ans
        
        q.put(vf)
        visited[vf] = True

        while q.empty() is False:
            front = q.get()
            for i in range(self.n):
                if self.adjMatrix[front][i] == 1 and visited[i] is False:
                    mapp[i] = front
                    q.put(i)
                    visited[i] = True

                    if i == vs:
                        ans = []
                        ans.append(vs)
                        value = mapp[vs]

                        while value != vs:
                            ans.append(value)
                            p = mapp[value]
                            value = p
                        ans.append(value)
                        return ans
        return []    

    def getPathBFS(self,vf,vs):
        if vf > self.n -1 or vs > self.n -1:
            return list() 
        visited =  [False for i in range(self.n)]
        return self.getPathBFSHelper(vf,vs,visited)

        
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
    ele = []
    ele = [int(element) for element in list(input().strip().split(" "))]
    vf = ele[0]
    vs = ele[1]
    return nv,ne,arr,vf,vs


nv,ne,arr,vf,vs = takeInput()
g = Graph(nv,ne)
i= 0
j= 0
while i < nv and j < ne:
    g.addEdge(arr[i][0],arr[i][1])
    i+=1
    j+=1

ans = g.getPathBFS(vf,vs)
if ans!= None:
    for ele in ans:
        print(ele,end=' ')