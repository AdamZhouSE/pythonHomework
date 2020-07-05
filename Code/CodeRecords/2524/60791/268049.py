class Node(object):
    def __init__(self, data = -1, lchild = None, rchild = None):
        self.data = data
        self.left = lchild
        self.right = rchild


def add(temp,root):
    if(temp.data < root.data and root.left == None):
        root.left = temp
    elif(temp.data >= root.data and root.right == None):
        root.right = temp
    elif(temp.data < root.data and root.left != None):
        add(temp,root.left)
    elif(temp.data >= root.data and root.right != None):
        add(temp,root.right)
    return
def output(root):
    print(root.data,end = ' ')
    while(root.left!=None):
        output(root.left)
        break
    if(root.right!=None):
        output(root.right)
    return
    
n = int(input())
arr = [int(i) for i in input().split(' ')]
root = Node(arr[0])
for i in range(1,len(arr)):
    temp = Node(arr[i])
    add(temp,root)
output(root)