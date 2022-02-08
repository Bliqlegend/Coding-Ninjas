def deleteNode(head,index):
    curr = head
    prev = None
    count = 0
    if head is None:
        return None
    if index == 0:
        return head.next
    while curr is not None:
        if count == index:
            if curr.next is None:
                curr = prev
                prev.next = None
            else:
                prev.next = curr.next
                curr = curr.next.next
        count+=1
        prev = curr
        curr = curr.next
    return head

def skipMdeleteN(head,M,N):
    count = 0
    curr = head
    while curr is not None:
        
    if count == M:
        idx = 0
        while idx <= N:
            deleteNode(curr)
            curr = curr.next
