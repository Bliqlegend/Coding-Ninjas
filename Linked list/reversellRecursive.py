import ll

def SreverseLL(head):
    if head is None or head.next is None:
        return head,head
    newhead , newtail = SreverseLL(head.next)
    newtail.next = head
    head.next = None
    return newhead,head

def OreverseLL(head):
    if head is None:
        return None
    if head.next is None:
        return head
    sh = OreverseLL(head.next)
    curr = sh
    while curr.next is not None:
        curr= curr.next
    curr.next = head 
    head.next = None 
    return sh

def reverse3(head):
    if head is None or head.next is None:
        return head
    sh = reverse3(head.next)   
    tail = head.next
    tail.next = head
    head.next = None
    return sh

head = ll.StakeInput()
head = reverse3(head)
ll.printLL(head)