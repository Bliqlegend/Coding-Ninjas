# Write your code here
class Graph:
    def __init__(self,nVertices,ne):
        self.ne = ne
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


nv,ne,arr,v1,v2 = takeInput()
g = Graph(nv,ne)
i= 0
j= 0
while i < nv and j < ne:
    g.addEdge(arr[i][0],arr[i][1])
    i+=1
    j+=1

def getPath(v1,v2):
    if g.hasPath(v1,v2):
        return
    else:
        return None


ans = getPath(v1,v2)
if ans != None:
    print()