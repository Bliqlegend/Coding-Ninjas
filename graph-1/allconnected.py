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

    def allCPHelper(self,visited,v,so):
        visited[v] = True
        so.append(v)

        for i in range(self.n):
            if self.adjMatrix[v][i] == 1 and not visited[i]:
                self.allCPHelper(visited,i,so)
        return so

    def allCP(self):
        visited = [False for i in range(self.n)]
        output= list()
        for i in range(self.n):
            if not visited[i]:
                so = list()
                self.allCPHelper(visited,i,so)
                output.append(so)
        return output

arr1=[int(x) for x in input().split()]
v=arr1[0]
p=Graph(v) 
for i in range(arr1[1]):
    arr2=[int(x) for x in input().split()]
    p.addEdge(arr2[0],arr2[1])

o = p.allCP()
for ele1 in o:
    ele1.sort()
    for ele2 in ele1:
            print(ele2,end=' ')
    print()
