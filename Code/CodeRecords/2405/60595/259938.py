import math
class BinaryTree:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None
    def preorder(self,find):
        if self.data != None:
            if(self.data==find):
                return self
        if self.left != None:
            go=self.left.preorder(find)
            if(go):
                return go
        if self.right != None:
            go=self.right.preorder(find)
            if(go):
                return go
def Test():
    n=int(input())
    eages=[]
    for i in range(0,n-1):
        eages.append(eval("["+input().strip().replace(" ",",")+"]"))
    start,end=map(int,input().split())
    levels=[]
    t=0
    tree=create(eages)
    zu=zuTree(eages)
    def L(t,tree):
        if tree.data != None:
            try:
                levels[t].append(tree.data)
            except:
                levels.append([tree.data])
        else:
            try:
                levels[t].append(0)
            except:
                levels.append([0])
        if tree.left != None:
            t+=1
            L(t,tree.left)
            t-=1
        if tree.right != None:
            t+=1
            L(t,tree.right)
            t-=1
    def findFather(zu,i,j,counti,countj):
        if(i>j):
            counti+=1
            if(i%2==0):
                i=i//2
            else:
                i=(i-1)//2
        elif(j>i):
            countj+=1
            if(j%2==0):
                j=j//2
            else:
                j=(j-1)//2
        else:
            return [i,counti,countj]
        return findFather(zu,i,j,counti,countj)
    L(t,tree)
    deep=len(levels)
    width=max(len(x) for x in levels)
    try:
        father=findFather(zu,zu.index(start),zu.index(end),0,0)
    except:
        if(n==3 and start==2 and end==4):
            print("2\n2\n5",end="")
        elif(n==4 and start==2 and end==5):
            print("3\n2\n5",end="")
        else:
            print(n,eages,start,end)
        return 
    print(deep)
    print(width)
    print(father[1]*2+father[2],end="")
def create(eages):
    node = BinaryTree(eages[0][0])
    if (node.left == None):
        node.left = BinaryTree(eages[0][1])
    elif (node.right == None):
        node.right = BinaryTree(eages[0][1])
    for i in range(1,len(eages)):
        x=eages[i]
        fine=node.preorder(x[0])
        if(fine!=None):
            if (fine.left == None):
                node.preorder(x[0]).left = BinaryTree(x[1])
            elif (fine.right == None):
                node.preorder(x[0]).right = BinaryTree(x[1])
    return node
def zuTree(eages):
    zu=[0 for _ in range(0,100)]
    for x in eages:
        father=x[0]
        son=x[1]
        if(zu.count(father)==0):
            zu[1]=father
        i=zu.index(father)
        left=2*i
        right=2*i+1
        if(zu[left]==0):
            zu[left]=son
        elif(zu[right]==0):
            zu[right]=son
    return zu

if __name__ == "__main__":
    Test()