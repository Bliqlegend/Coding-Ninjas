from locale import currency
import ll

def lengthofLL(head):
    curr = head
    l = 0
    while curr is not None:
        l+=1
        curr = curr.next
    return l
    
head = ll.StakeInput()
l = lengthofLL(head)
print(l)