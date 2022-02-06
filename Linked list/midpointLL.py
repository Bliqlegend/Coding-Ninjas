import ll

def lengthofLL(head):
    curr = head
    l = 0
    while curr is not None:
        l+=1
        curr = curr.next
    return l
    

def TRASH(head):
    mp = (lengthofLL(head) - 1)/ 2
    curr = head
    count = 0
    while curr is not None:
        if count == mp:
            return curr.data
        curr = curr.next
        count+=1


def midPoint(head):
    if head is None:
        return None
    slow=head
    fast =head
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        fast = fast.next.next
    return slow

head = ll.StakeInput()
slow = midPoint(head)
if slow is None:
    print(None)
else:
    print(slow.data)