import ll


def TAswapNodes(head,i,j):
    if i == j:
        return head
    curr = head
    prev = None
    c1 = None
    c2 = None
    p1 = None
    p2 = None
    pos = 0
    while curr is not None:
        if pos == i:
            p1 = prev
            c1 = curr
        elif pos == j:
            p2 = prev
            c2 = curr
        prev = curr
        curr = curr.next
    if p1 is not None:
        p1.next = c2
    else:
        head = c2
    if p2 is not None:
        p2.next = p1
    else:
        head = c1
    
    curr1 = c2.next
    c2.next = c1.next
    c1.next = curr1
    return head

head = ll.StakeInput()
