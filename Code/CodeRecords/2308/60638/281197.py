class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def find(numbers,n):
    for i in range(0,len(numbers)):
        if numbers[i][0]==n:
            return i
def inpox(res,root):
    if root==None:
        return None
    inpox(res,root.left)
    res.append(root.val)
    inpox(res,root.right)

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
nums=list(map(int,input().split(" ")))
n=nums[0]
numbers=[]
for x in range(0,n):
    numbers.append(list(map(int,input().split(" "))))
m=int(input())
root=creatTree(numbers,0)
res=[]
inpox(res,root)
k=-1
for i in range(0,len(res)):
    if res[i]==m:
        k=i
        break
if k==len(res)-1:
    print(0)
else:
    print(res[k+1])