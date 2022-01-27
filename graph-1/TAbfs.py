import queue
class Graph:
    def __init__(self, nVertices):
        self.vertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def bfs(self,visited,sv):
        #visited = [False for i in range(self.vertices)]
        q = queue.Queue()
        q.put(sv)
        while not q.empty():
            node = q.get()
            print(node, end=' ')
            visited[node] = True
            for i in range(self.vertices):
                if self.adjMatrix[node][i] == 1 and visited[i] is False:
                    visited[i] = True
                    q.put(i)

        
l = [int(x) for x in input().strip().split()]
vertices = l[0]
edges = l[1]

g = Graph(vertices)

for i in range(edges):
    edgPair = [int(x) for x in input().strip().split()]
    g.addEdge(edgPair[0], edgPair[1])
visited = [False for i in range(vertices)]
for i in range(vertices):
    if visited[i] is False:
        g.bfs(visited,i)