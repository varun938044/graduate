def insertNodeAtTail(head, data):
    newBlock = SinglyLinkedListNode(data)

    if head == None:
        return newBlock

    curr = head 
    while curr.next!= None:
        curr = curr.next
    curr.next = newBlock
    return head
