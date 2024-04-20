def insertNodeAtPosition(llist, data, position):
    newBlock = SinglyLinkedListNode(data)
    if position == 1:
        newBlock.next = llist
        return newBlock
    index = 1 
    curr = llist
    while index != position:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return llist
     
 
    
