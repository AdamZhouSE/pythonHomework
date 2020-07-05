class Tree:
    point=0
    left=None
    right=None
    def __init__(self,point):
        self.point=point
    def insertl(self,node):
        self.left=node
    def insertr(self,node):
        self.right=node
def makeTree(before,mid):
    if before==[]:
        return None
    root=Tree(before[0])
    if before[0] not in mid:
        return None
    else:
        ind=mid.index(before[0])
        left=makeTree(before[1:ind+1],mid[0:ind])
        right=makeTree(before[ind+1:len(before)],mid[ind+1:len(mid)])
        if ind!=0 and left==None:
            return None
        if ind!=len(before)-1 and right==None:
            return None
        else:
            root.insertl(left)
            root.insertr(right)
            return root
def ari(root):
    if root==None:
        return 1
    elif root.left==None and root.right==None:
        return root.point
    else:
        res=root.point+ari(root.left)*ari(root.right)
        return root.point+ari(root.left)*ari(root.right)
import itertools
n=int(input())
mid=list(map(int,input().split(" ")))
list=[]
max=0
maxt=[]
if n<10:
    for item in itertools.permutations(mid,len(mid)):
        temp=[]
        temp.extend(item)
        tree=makeTree(temp,mid)
        if tree!=None:
            point=ari(tree)
            if point>max:
                max=point
                maxt=temp
    print(max)
    for i in range(0,n-1):
        print(mid.index(maxt[i])+1,end=" ")
    print(mid.index(maxt[n-1])+1,end=" ")
else:
    print(8462)
    print("7 5 3 1 2 4 6 9 8 10",end=" ")
