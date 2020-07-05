import queue
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.lev=1
nums=list(map(int,input().split(" ")))

n=nums[0]
numbers=[]
root=TreeNode(nums[1])
treeRoot=root
nodeList=[0]*(10000)
nodeList[nums[1]]=root
for i in range(0,n):
    nums=list(map(int,input().split(" ")))
    
    root=nodeList[nums[0]]
    if nums[1]!=0:
        root.left=TreeNode(nums[1])
        root.left.lev=root.lev+1
        nodeList[nums[1]]=root.left
    if nums[2]!=0:
        root.right=TreeNode(nums[2])
        root.right.lev=root.lev+1
        nodeList[nums[2]]=root.right
q=queue.Queue()
q.put(treeRoot)
result=[]
levs=[]
while not q.empty():
    root=q.get()
    result.append(root)
    levs.append(root.lev)
    if root.left!=None:
        q.put(root.left)
    if root.right!=None:
        q.put(root.right)
for i in range(1,max(levs)+1):
    print("Level ",end="")
    print(i,":",end="")
    for j in range(0,n):
        if levs[j]==i:
            print("",result[j].val,end="")
    print()
point =False
for i in range(1,max(levs)+1):
    print("Level ",end="")
    print(i,end="")
    if not point:
        print(" from left to right:",end="")
        for j in range(0,n):
            if levs[j]==i:
                print("",result[j].val,end="")
        print()
    else:
        print(" from right to left:", end="")
        for j in range(0, n):
            if levs[n-1-j] == i:
                print("", result[n-1-j].val, end="")
        print()
    point=not point
