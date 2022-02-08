from email.headerregistry import HeaderRegistry
import ll

def TRASH(head):
    fh = ll.Node(0)
    ft = fh
    curr1 = head
    curr2 = head
    
    while curr1 is not None:
        if curr1.data % 2 != 0:
            ft.next = curr1
            ft = ft.next
            curr1 = curr1.next
        else:
            curr1 = curr1.next

    while curr2 is not None:
        print("loop me ghus gaye")
        print(curr2.data)
        if curr2.data % 2 == 0:
            print("aa to gaye")
            ft.next = curr2
            ft = ft.next
            curr2 = curr2.next
        else:
            print(f"even nahi mila {curr2.data} pe")
            curr2 = curr2.next
    return fh.next

def evenodd(head):
    oh , ot = None,None
    eh , et = None,None
    if head is None:
        return None,None
    curr = head
    while curr is not None:
        if curr.data % 2 == 0:
            if et is not None:
                et.next = curr
                et = et.next
            else:
                et = curr
                eh = curr
            curr = curr.next   
        else:
            if ot is not None:
                ot.next = curr
                ot = ot.next
            else:
                ot = curr
                oh = curr
            curr = curr.next   
    if et is None:
        return head
    if ot is None:
        return head
    
    et.next = None
    ot.next = None
    ot.next = eh
    return oh


head = ll.StakeInput()
head = evenodd(head)
ll.printLL(head)