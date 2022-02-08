def evenAfterOdd(head) :
    curr = head
    oh,ot = None,None
    eh,et = None,None
    while curr is not None:
        if curr.data %2 == 0:
            if eh is not None:
                et.next = curr
                et = et.next 
            else:
                eh = curr
                et = curr
            curr = curr.next
        else:
            if oh is not None:
                ot.next = curr
                ot = ot.next
                
            else:
                oh = curr
                ot = curr
            curr = curr.next
     
    if et is None:
        return head
    if ot is None:
        return head
                
    et.next = None
    ot.next = None
    ot.next = eh
    return oh