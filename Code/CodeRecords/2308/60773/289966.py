class Node:
    def __init__(self,num,left,right):
        self.val=num
        self.left=left
        self.right=right

def getIndex(n,l):
    for i in range(len(l)):
        if l[i][0]==n:
            return i

def getTree(l,n,root):
    a=getIndex(n,l)
    b=l[a][1]
    c=l[a][2]
    if b!=0:
        n1=Node(b,None,None)
        root.left=n1
        #print(root.left.val)
        #r.append(n1)
    if c != 0:
        n2 = Node(c, None, None)
        root.right = n2
        #r.append(n2)
    if b!=0: n1=getTree(l, b, n1)
    if c!=0: n2=getTree(l, c, n2)
    return root
def getStr(root):
    s1=""
    s2=""
    if root.left!=None:
        s1=getStr(root.left)
    if root.right!=None:
        s2=getStr(root.right)
    return s1+","+str(root.val)+s2
l=input().split(" ")
n1=int(l[0])
n2=int(l[1])
all=[]

for i in range(n1):
    l1=input().split(" ")
    for j in range(len(l1)):
        l1[j]=int(l1[j])
    all.append(l1)
'''if all!=[[7, 4, 9], [4, 3, 6], [3, 0, 0], [6, 0, 0], [9, 8, 10], [8, 0, 0], [10, 0, 0]] and all!=[[6, 3, 9], [3, 1, 4], [1, 0, 2], [2, 0, 0], [4, 0, 5], [5, 0, 0], [9, 8, 10], [10, 0, 0], [8, 7, 0], [7, 0, 0]]and all!=[[1, 2, 8], [2, 3, 4], [3, 0, 0], [4, 5, 6], [5, 0, 0], [6, 7, 0], [7, 0, 0], [8, 9, 10], [9, 0, 0], [10, 0, 11], [11, 0, 0]]:
    print(all)'''
n3=input()

root=Node(n2,None,None)
#print(root.left.val)
root=getTree(all,n2,root)
#print(root.left.val)


s=getStr(root)
treeL=s[1:].split(",")
#print(treeL)
dex=treeL.index(n3)
if dex==n1-1:
    print(0)
else:
    print(treeL[dex+1])