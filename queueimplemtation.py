# Queue implementation 
 
 
10, 20, 30, 40, 50 
 
# Enqueue --> insertion at tail 
# Dequeue --> deletion at head 
 
 
# Linked-list based implementation 
 
 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def enQueue(head, val):
    # This function inserts node at tail
    newBlock = Node(val)
    if head == None:
        return newBlock 
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock
    return head
 
def deQueue(head):
    # This function deletes first node
    if head == None:
        print("Queue is empty, nothing to delete")
        return None
 
    print("Deleting", head.data)
    secondNode = head.next 
    head.next = None 
    return secondNode
 
def printQueue(head):
    if head == None:
        print("Queue is empty")
        return 
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
head = None 
head = enQueue(head, 10)
head = enQueue(head, 20)
head = enQueue(head, 100)
 
printQueue(head)
# 10 --> 20 --> 100
 
head = deQueue(head)
# Deleting 10 
 
printQueue(head)
# 20 --> 100 
 
head = deQueue(head)
# Deleting 20 
 
printQueue(head)
# 100 
 
head = deQueue(head)
# Deleting 100 
 
printQueue(head)
#  Queue is empty
 
head = deQueue(head)
# Queue is empty, nothing to delete
 
 
 
 
 
 
 
 
 
 
 
