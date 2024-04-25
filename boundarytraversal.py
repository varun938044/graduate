class TreeNode:
    def _init_(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

        
def collectLeftBoundary(root, result):
    while root != None:
        if root.left == None and root.right == None:
            break
 
        result.append(root.data)
 
        if root.left != None:
            root = root.left 
        else:
            root = root.right

def collectLeafNodes(root, result):
    if root == None:
        return 
    if root.left == None and root.right == None:
        result.append(root.data)
        return
 
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)

def collectRightBoundaryInReverseDirection(root, result):
 
    temp = []
    while root != None:
        if root.left == None and root.right == None:
            break
 
        temp.append(root.data)
 
        if root.right != None:
            root = root.right 
        else:
            root = root.left
 
    temp = temp[::-1]
    for ele in temp:
        result.append(ele)

def printBoundaryTraversal(root):
    result = []
 
    result.append(root.data)
    # task-1: collect left boundary 
    collectLeftBoundary(root.left, result)
 
    # task-2: collect leaf nodes (in left to right direction)
    collectLeafNodes(root, result)
 
    # task-3: collect right boundary(in reverse direction)
    collectRightBoundaryInReverseDirection(root.right, result)
 
  
    print(*result)
 
 
# 1. objects creation (memory allocation) 
root = TreeNode(11)

obj2 = TreeNode(7)
obj3 = TreeNode(15)
obj4 = TreeNode(5)
obj5 = TreeNode(9)
obj6 = TreeNode(3)
obj7 = TreeNode(8)
obj8 = TreeNode(10)
obj9 = TreeNode(13)
obj10 = TreeNode(20)
obj11= TreeNode(12)
obj12= TreeNode(14)
obj13= TreeNode(18)
obj14= TreeNode(25)

 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj4.left = obj6

obj5.left = obj7
obj5.right = obj8

obj3.left = obj9
obj3.right = obj10

obj9.left = obj11
obj9.right = obj12

obj10.left = obj13
obj10.right = obj14

printBoundaryTraversal(root)
