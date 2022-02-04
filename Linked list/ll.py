class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
# Next is just a pointer
# Data is what we pass while calling

def printLL(head):
    curr = head
    while curr is not None:
        print(str(curr.data)+'->',end=' ')
        curr = curr.next
    print("None")
    return

def StakeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode 
    return head

def OtakeInput():
    # TC :O(n^2)
    inputList = [int(ele) for ele in input().split()]
    head = None
    
    for currData in inputList:
        if currData == -1:
            break    
        newNode = Node(currData)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode 

    return head
# input a list and move over it converting each element to a node adding to the linked list
# when -1 is entered it automatically breaks the pattern

# a = StakeInput()
# printLL(a)