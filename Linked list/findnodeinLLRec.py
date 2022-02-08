from gettext import find
import ll

def findNode(head,k,c):
    if head is None:
        return -1
    if head.data == k:
        return c
    return findNode(head.next,k,c+1)

head = ll.StakeInput()
k = int(input())
ans = findNode(head,k,0)
print(ans)