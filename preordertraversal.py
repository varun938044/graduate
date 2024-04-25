class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)
 

 
root = TreeNode(11)

obj2 = TreeNode(7)
obj3 = TreeNode(5)
obj4 = TreeNode(3)
obj5 = TreeNode(9)
obj6 = TreeNode(8)
obj7 = TreeNode(10)
obj8 = TreeNode(15)
obj9 = TreeNode(13)
obj10 = TreeNode(12)
obj11= TreeNode(14)
obj12= TreeNode(20)
obj13= TreeNode(18)
obj14= TreeNode(25)
 

root.left = obj2 
root.right = obj8
 
obj2.left = obj3
obj2.right = obj5 
 
obj3.left = obj4

obj5.left = obj6
obj5.right = obj7

obj8.left = obj9
obj8.right = obj12

obj9.left = obj10
obj9.right = obj11

obj12.left = obj13
obj12.right = obj14

printPreOrder(root)
