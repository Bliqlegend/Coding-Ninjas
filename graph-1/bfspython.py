import queue
class Graph:
    def __init__(self,n):
        self.n = n
        self.adjMatrix = [[0 for i in range(n)] for i in range(n)]

    def bfsHelper(self,sv,visited):
        q = queue.Queue()
        q.put(sv)
        while q.empty() is False:
            u = q.get()
            print(u,end='')
            visited[u] = True
            for i in range(self.n):
                if self.adjMatrix[sv][i] > 0 and visited[i] = False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):          
        visited = [False for i in range(self.n)]
        self.bfsHelper(0,visited)