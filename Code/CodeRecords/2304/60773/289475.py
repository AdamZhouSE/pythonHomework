class Node:
    def __init__(self,num,left,right):
        self.val=num
        self.left=left
        self.right=right

def getIndex(n,l):
    for i in range(len(l)):
        if l[i][0]==n:
            return i

def getTree(l,n,root,r):
    a=getIndex(n,l)
    b=l[a][1]
    c=l[a][2]
    if b!=0:
        n1=Node(b,None,None)
        root.left=n1
        r.append(n1)
    if c != 0:
        n2 = Node(c, None, None)
        root.right = n2
        r.append(n2)
    if b!=0: n1=getTree(l, b, n1,r)
    if c!=0: n2=getTree(l, c, n2,r)
    if b==0 and c==0:
        return root

l=input().split(" ")
n1=int(l[0])
n2=int(l[1])
all=[]
leaf=[]

for i in range(n1):
    l1=input().split(" ")
    for j in range(len(l1)):
        l1[j]=int(l1[j])
    all.append(l1)
#print(all)

count=0
root=Node(n2,None,None)
leaf.append(root)
root=getTree(all,n2,root,leaf)

put=[]
num=[]
for i in range(n1):
    num.append(0)
m=getIndex(n2,all)
num[m]=1
for i in range(n1):
    if all[i][1] !=0:
        num[getIndex(all[i][1],all)]=num[getIndex(all[i][0],all)]+1
    if all[i][2] !=0:
        num[getIndex(all[i][2], all)] = num[getIndex(all[i][0], all)] + 1
#print(num)
ma=max(num)
pall=[]
for i in range(ma):
    pall.append(0)
for i in range(n1):
    pall[num[i]-1]=pall[num[i]-1]+1
#print(pall)
queue=[n2]
for i in range(n1):
    w1=all[getIndex(queue[i],all)][1]
    w2 = all[getIndex(queue[i],all)][2]
    if w1!=0:
        queue.append(w1)
    if w2!=0:
        queue.append(w2)
#print(queue)
start=0
end=0
for i in range(ma):

    print("Level ",end="")
    print(i+1,end="")
    print(" :",end="")
    for j in range(pall[i]):
        print("",end=" ")
        print(queue[start+j],end="")
    start=start+pall[i]
    print("")
start=0
for i in range(ma):
    end=end+pall[i]
    print("Level ", end="")
    print(i + 1, end=" ")
    if i%2==0:
        print("from left to right:",end="")
        for j in range(pall[i]):
            print("",end=" ")
            print(queue[start + j], end="")
    else:
        print("from right to left:",end="")
        for j in range(pall[i]):
            print("",end=" ")
            print(queue[end-1-j], end="")
    start = start + pall[i]
    print("")
