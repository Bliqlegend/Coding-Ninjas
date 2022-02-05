import ll

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

head = ll.StakeInput()
index = int((input()))
head = deleteNode(head,index)
ll.printLL(head)