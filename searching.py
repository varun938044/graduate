class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,ele):
    if root==None:
        newblock=node(ele)
        return newblock

    if root.data<ele:
        root.right=insert(root.right,ele)
    else:
        root.left=insert(root.left,ele)
    return root                

def inorder(root):
    if root==None:
        return
    inorder(root.left)    
    print(root.data,end=" ")
    inorder(root.right) 
    
    
def search(root,target):
    if root==None:
        return False
    elif root.data==target:
        return True
    elif root.data<target:
        return search(root.right,target)
    return search(root.left,target)       
        

n=int(input())
nums=list(map(int,input().split()))
target=int(input())
root=None
for ele in nums:
    root=insert(root,ele)
    
if search(root,target)==True:
    print("Target element is found")
else:
    print ("Target element is not found")
