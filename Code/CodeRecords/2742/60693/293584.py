import copy
class Tree:
    def __init__(self):
        self.elements=[]

    def insert(self,x:int):
        self.elements.append(x)
        self.elements.sort()

    def delete(self,x:int):
        self.elements.remove(x)

    def findXOrder(self,x:int):
        return self.elements.index(x)+1

    def findxth(self,x:int):
        return self.elements[x-1]

    def getPre(self,x:int):
        if self.elements[0]>=x:
            return -2147483647
        arrlen=len(self.elements)
        for i in range(arrlen):
            if self.elements[i]>=x:
                return self.elements[i-1]
        return self.elements[-1]

    def getNext(self,x:int):
        if self.elements[-1]<=x:
            return 2147483648
        arrlen = len(self.elements)
        for i in range(arrlen):
            if self.elements[i] > x:
                return self.elements[i]
    
    def printTree(self):
        print(self.elements)

tree_ver=[]
v0=Tree()
tree_ver.append(v0)
n=int(input())
for _ in range(n):
    ope=list(map(int,input().split()))
    v,o,x=ope[0],ope[1],ope[2]
    newTree=copy.deepcopy(tree_ver[v])
    if o==1:
        newTree.insert(x)
    if o==2:
        newTree.delete(x)
    if o==3:
        res=newTree.findXOrder(x)
        print(res)
    if o==4:
        res=newTree.findxth(x)
        print(res)
    if o==5:
        res=newTree.getPre(x)
        print(res)
    if o==6:
        res=newTree.getNext(x)
        print(res)
    tree_ver.append(newTree)