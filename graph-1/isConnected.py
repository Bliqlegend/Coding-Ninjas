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


nv,ne,arr = takeInput()
if nv == 0:
    print('true')
else:
    g = Graph(nv)
    i= 0
    j= 0
    while i < nv and j < ne:
        g.addEdge(arr[i][0],arr[i][1])
        i+=1
        j+=1

    if g.isConnected():
        print("true")
    else:
        print("false")