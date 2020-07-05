class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def find(numbers,n):
    for i in range(0,len(numbers)):
        if numbers[i][0]==n:
            return i
def creatTree(numbers,i):
    if i==len(numbers):
        return None
    root=TreeNode(numbers[i][0])
    if numbers[i][1]!=0:

        root.left=creatTree(numbers,find(numbers,numbers[i][1]))
    if numbers[i][2]!=0:
        i=find(numbers,numbers[i][2])
        root.right=creatTree(numbers,i)
    return root
def inTree(res,root):
    if root==None:
        return None
    inTree(res,root.left)
    res.append(root.val)
    inTree(res,root.right)
def preTree(res,root):
    if root==None:
        return None
    res.append(root.val)
    preTree(res,root.left)
    preTree(res,root.right)
def postTree(res,root):
    if root==None:
        return None
    postTree(res,root.left)
    postTree(res,root.right)
    res.append(root.val)
def printAll(numbers):
    for i in range(0,len(numbers)):
        print(numbers[i],end=" ")
nums=list(map(int,input().split(" ")))
n=nums[0]
numbers=[]
for x in range(0,n):
    numbers.append(list(map(int,input().split(" "))))
root=creatTree(numbers,0)
resIn=[]
resPre=[]
resPost=[]
inTree(resIn,root)
preTree(resPre,root)
postTree(resPost,root)
printAll(resPre)
print()
printAll(resIn)
print()
for i in range(0,len(resPost)-1):
    print(resPost[i],end=" ")
print(resPost[-1])