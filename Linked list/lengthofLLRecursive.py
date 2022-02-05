import ll

def lengthRecursive(head,l):
    if head is None:
        return 0
    if head.next is None:
        return 1
    return 1 + lengthRecursive(head.next,l+1) 

head = ll.StakeInput()
l = lengthRecursive(head,0)
print(l)
