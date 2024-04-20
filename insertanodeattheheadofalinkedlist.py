def insertNodeAtHead(llist, data):
    newBlock = SinglyLinkedListNode(data)
    if llist == None:
        return newBlock
    newBlock.next = llist
    return newBlock
