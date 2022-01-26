from more_itertools import take
from bfs import Graph


def hasPath(vf,vs):
    if g.hasPathHelper(vf,vs):
        return True
    else:
        arr = g.cel(vf)
        for i in arr:
            if g.hasPathHelper(i,vs):
                return True
    return False

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
# g = Graph(5,5)
# g.addEdge(0,1)
# g.addEdg
g = Graph(nv,ne)
i= 0
j= 0
while i < nv and j < ne:
    g.addEdge(arr[i][0],arr[i][1])
    i+=1
    j+=1

ans = hasPath(vf,vs)
if ans==True:print("true")
else: print("false")