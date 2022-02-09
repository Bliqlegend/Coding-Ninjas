from ll import *

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

def TRASH(head,M,N):
    count = 0
    curr = head
    while curr is not None:
        return
    if count == M:
        idx = 0
        while idx <= N:
            deleteNode(curr,count)
            curr = curr.next

def skip(head,m,n):
    if m == 0 or head is None:
        return None
    if n == 0:
        return head
    c1 = 1
    c2 = 1
    t1,t2 = head,head
    curr = head 
    while curr is not None:
        if t1 == m:
            t2 = t1.next
            while c2 != n and t2 is not None:
                t2= t2.next
                c2+=1
            t2 = t2.next
            t1 = t2
            # count reset
            c1 = 1
            c2 = 1
        else:
            t1 = t1.next
            c1+=1
        curr = curr.next
    return head

def skiptake(head,m,n):
    if m == 0 or head is None:
        return None
    if n == 0:
        return head
    curr = head
    temp = None
    while curr is not None:
        take = 0
        skip = 0
        while curr is not None and take < m:
            if temp is None:
                temp = curr
            else:
                temp.next = curr
                temp = curr
            curr = curr.next
            take+=1
        
        while curr is not None and skip < n:
            curr = curr.next
            skip+=1
    if temp is not None:
        temp.next = None

    return head

head = StakeInput()
m,n = 2,2
newh = skiptake(head,m,n)
printLL(newh)
