import ll
def RinsertatI(head,index,newnode):
    if index < 0:
        return head
    if index == 0:
        newnode.next = head
        return newnode

    if head is None:
        return None
    smallhead = RinsertatI(head.next,index-1,newnode)
    head.next = smallhead
    return head

def insertatI(head,index,newnode):
    curr = head
    prev = None
    count = 0
    while curr is not None:
        if count == index:
            prev.next = newnode
            newnode.next = curr
            curr = newnode
        prev = curr
        curr = curr.next
        count+=1
    return head

head = ll.StakeInput()
index = int(input())
newdata = int(input())
newnode = ll.Node(newdata)
RinsertatI(head,index,newnode)
ll.printLL(head)