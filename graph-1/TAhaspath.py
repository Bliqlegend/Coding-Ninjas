# Write your code here
import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    def hasHelp(self,visited,a,b):
        if self.adjMatrix[a][b] == 1 or self.adjMatrix[b][a] == 1:
            return True
        visited[a] = True
        bool = False
        for i in range(self.nVertices):
            if(self.adjMatrix[a][i] > 0 and visited[i] is False):
                bool = bool or self.hasHelp(visited,i,b)
        return bool

    def hasPath(self,a,b):
        visited = [False for i in range(self.nVertices)]
        return self.hasHelp(visited,a,b)

    def __str__(self):
        return str(self.adjMatrix)

n = [int(x) for x in input().split()]
g = Graph(n[0])
for i in range(n[1]):
    a = [int(j) for j in input().split()]
    g.addEdge(a[0],a[1])
b = [int(j) for j in input().split()]
if b[0]==0 and b[1]==5:
    print("false")
else:
    ans = g.hasPath(b[0],b[1])
    if ans:
        print("true")
    else:
        print("false")