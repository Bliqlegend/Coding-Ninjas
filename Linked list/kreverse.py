from ll import *

def kreverse(head,k):
    if k == 0 or k == 1:
        return head
    curr = head
    prev = None
    necxt = None
    count = 0
    while count<k and curr is not None:
        necxt = curr.next
        curr.next = prev
        prev = curr
        curr = necxt
        count+=1
    
    if necxt is not None:
        head.next = kreverse(necxt,k)
    return prev


head = StakeInput()
k = int(input())
newh = kreverse(head,k)
printLL(newh)