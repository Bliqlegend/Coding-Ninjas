from types import new_class
from ll import *

def bubblesort(head):
    if head is None:
        return None
    curr = head
    while curr is not None:
        i = curr.next
        while i is not None:
            if curr.data > i.data:
                # we do a data swap
                temp = curr.data
                curr.data = i.data
                i.data = temp
            i = i.next
        curr = curr.next
    return head
    

head = StakeInput()
newH = bubblesort(head)
printLL(newH)
