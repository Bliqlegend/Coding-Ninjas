import ll

def lengthofLL(head):
    curr = head
    l = 0
    while curr is not None:
        l+=1
        curr = curr.next
    return l  

def deleteMiddle(head):
    if head is None or head.next is None:
        return None
    L = lengthofLL(head)
    if L % 2 == 0:
        c = (L//2)-1
    else:
        c = (L//2)
    if c==0:
        head = head.next
        return head
    curr = head
    prev = None
    count = 0
    while curr is not None:
        if count == c:
            if curr.next is None:
                curr = prev
                prev.next = None
                break
            else:
                prev.next = curr.next
                curr = curr.next.next
                break
        else:
            prev = curr
            curr = curr.next
            count+=1
    return head

head = ll.StakeInput()
head = deleteMiddle(head)
ll.printLL(head)