import queue
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __getPathDFS(self, sv, ev, visited):
        if sv == ev:
            return list([sv])

        visited[sv] = True

        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                li = self.__getPathDFS(i, ev, visited)

                if li != None:
                    li.append(sv)
                    return li

        return None
    def getPathDFS(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathDFS(sv, ev, visited)


    def removeEdge(self,v1,v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else:
            return False
    def __getPathBFS(self, sv, ev, visited):
        mapp = {}
        q = queue.Queue()

        if self.adjMatrix[sv][ev] == 1 and sv == ev:
            ans = []
            ans.append(sv)
            return ans

        q.put(sv)
        visited[sv] = True

        while q.empty() is False:
            front = q.get()

            for i in range(self.nVertices):
                if self.adjMatrix[front][i] == 1 and visited[i] is False:
                    mapp[i] = front
                    q.put(i)

                    visited[i] = True

                    if i == ev:
                        ans = []
                        ans.append(ev)
                        value = mapp[ev]

                        while value != sv:
                            ans.append(value)
                            value = mapp[value]

                        ans.append(value)
                        return ans

        return []

    def getPathBFS(self, sv, ev):

        # Return empty list in case sv or ev is invalid
        if (sv > (self.nVertices - 1)) or (ev > (self.nVertices - 1)):
            return list()
        visited = [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)

    def _str_(self):
        return str(self.adjMatrix)


arr=[int(i) for i in input().split()]
V=arr[0]
E=arr[1]
g = Graph(V)

for i in range(E):
    arr=[int(j) for j in input().split()]
    a=arr[0]
    b=arr[1]
    g.addEdge(a,b)

arr=[int(i) for i in input().split()]
V1=arr[0]
V2=arr[1]


li = g.getPathBFS(V1, V2)

if li != None:
    for element in li:
        print(element, end=' ')