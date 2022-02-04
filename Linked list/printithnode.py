import ll

def printIthNode(head,index):
    curr = head
    idx=0
    while curr is not None:
        if idx == index:
            print(curr.data)
            return
        idx+=1
        curr = curr.next
    return
    
head = ll.StakeInput()
index = int(input())
printIthNode(head,index)

