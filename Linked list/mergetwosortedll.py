def merge(head1,head2):
    if head1 == None:
        return None
    if head2 == None:
        return None
    if head1.data < head2.data:
        newHead = head1
        newTail = head1
        head1 = head1.next
    else:
        newHead = head2
        newTail = head2
        head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            newTail.next = head1
            newTail = newTail.next
            head1 = head1.next
        else:
            newTail.next = head2 
            newTail = newTail.next
            head2 = head2.next
    if head1 is not None:
        newTail.next = head1
    if head2 is not None:
        newTail.next = head2
    return newHead    


