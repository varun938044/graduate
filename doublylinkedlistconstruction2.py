# 51 --> 52 --> 53 --> 54 --> 55 --> 56 --> 57 --> 58 --> 59 --> None
# None<--  <--     <--    <--    <--    <--    <--    <--    <--
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(tail):
    print("Right to Left")
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 
 
 
# object creation    
obj1 = Node(121)
obj2 = Node(145)
obj3 = Node(678)
obj4 = Node(89)
obj5 = Node(12)
 
# links establishments
obj1.next = obj2 
obj2.prev = obj1 
 
obj2.next = obj3 
obj3.prev = obj2 
 
obj3.next = obj4 
obj4.prev = obj3 
 
obj4.next = obj5 
obj5.prev = obj4 
 
printLeftToRightManner(obj1)
printRightToLeftManner(obj5)
 
 
 
 
 
 
 
# During object creation, the constructor executes automatically
 
 
 
 
