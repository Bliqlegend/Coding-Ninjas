import ll

def lengthofLL(head):
    curr = head
    l = 0
    while curr is not None:
        l+=1
        curr = curr.next
    return l  


def nthNodeFromend(head,n):
    L = lengthofLL(head)
    m = L - n
    count = 0
    curr = head
    while curr is not None:
        if count == m:
            print(curr.data)
            return
        count+=1
        curr = curr.next
    return None


head = ll.StakeInput()
n = int(input())
nthNodeFromend(head,n)
