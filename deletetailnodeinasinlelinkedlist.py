class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    head = None
    for data in arr:
        head = insertNodeAtEnd(head, data)
    return head

def insertNodeAtEnd(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next

def deleteLastNode(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return head

n = int(input())
a= list(map(int, input().split()))

head = createLinkedList(a)

printLinkedList(head)
head = deleteLastNode(head)
print()
printLinkedList(head)
