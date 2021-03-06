from pydoc import visiblename


class Graph:
    def __init__(self,n):
        self.n = n
        self.adjMatrix = [[0 for j in range(n)] for i in range(n)]
    
    def dfsHelper(self,sv,visited):
        visited[sv] = True
        for i in range(self.n):
            if self.adjMatrix[sv][i] == 1 and visited[i] is False:
                self.dfsHelper(i,visited)
                visited[i] = True
        
    # def dfs(self):
    #     visited = [False for i in range(self.n)]
    #     Nvisited = self.dfsHelper(0,visited)
    #     return Nvisited
    
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] =1
        self.adjMatrix[v2][v1] = 1
    
    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v2] = 0
        
    def __str__(self):
        return str(self.adjMatrix)

    def isConnected(self):
        visited = [False for i in range(self.n)]
        self.dfsHelper(0,visited)
        for bool in visited:
            if bool is False:
                return False
        return True

arr1=[int(x) for x in input().split()]
v=arr1[0]
if v == 0:
    print('true')
else:
    p=Graph(v) 
    for i in range(arr1[1]):
        arr2=[int(x) for x in input().split()]
        p.addEdge(arr2[0],arr2[1])
    if p.isConnected():
        print("true")
    else:
        print("false")