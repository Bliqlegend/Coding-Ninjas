class Edge:
    def __init__(self,src,dest,wt) -> None:
        self.src = src
        self.dest = dest
        self.wt = wt
    

li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
edges = []

def kruskal(edge,n):
    parent = [i for i in range(n)]
    

for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src,dest,wt)
    edges.append(edge)

output = kruskal(edge,n)