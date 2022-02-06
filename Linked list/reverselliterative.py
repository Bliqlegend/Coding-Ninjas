import ll

def reverse(head):
    if head is None:
        return None
    curr = head
    prev = None
    while curr is not None:
        necxt = curr.next
        curr.next = prev
        prev = curr
        curr = necxt
        # next is saving the next node not just the address but the whole node
        # at the end of this curr will be at None and prev will be at last node which is the new head
    head = prev
    return head


head = ll.StakeInput()
head = reverse(head)
ll.printLL(head)