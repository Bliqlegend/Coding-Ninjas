from telnetlib import NEW_ENVIRON
import ll

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
insertatI(head,index,newnode)
ll.printLL(head)