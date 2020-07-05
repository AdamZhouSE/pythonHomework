import math
class Node(object):
    def __init__(self):
        self.l=0
        self.x=0
        self.y=0

edges=[Node() for i in range(0,2**16)]
fa=[0 for i in range(0,2**16)]
total=0
k=0
a=[0 for i in range(2**16)]
b=[0 for i in range(2**16)]
def kruskal(m):
    global fa
    global k
    global total
    for i in range(1,m+1):
        l=find(edges[i].fir)
        r=find(edges[i].sec)
        if l==r:
            continue
        else:
            fa[l]=r
        k=edges[i].val
        total+=1
        if total==m-1:
            break

def find(x):
    global fa
    if x!=fa[x]:
        fa[x]=find(fa[x])

    return fa[x]

def unity(x,y):
    global fa
    r1=find(x)
    r2=find(y)
    fa[r1]=r2

if __name__=='__main__':
    row=input().split(" ")
    S=int(row[0])
    P=int(row[1])
    for i in range(1,P+1):
        row=input().split(" ")
        a[i]=int(row[0])
        b[i]=int(row[1])
        for j in range(1,i):
            k+=1
            edges[k].l=math.sqrt((a[i]-a[j])**2+(b[i]-b[j])**2)
            edges[k].x=i
            edges[k].y=j
    for i in range(1,P+1):
        fa[i]=i
    temp=sorted(edges[1:k+1],key=lambda x:x.l)
    edges[1:k+1]=temp
    for i in range(1,k+1):
        if find(edges[i].x)!=find(edges[i].y):
            unity(edges[i].x,edges[i].y)
            ans=edges[i].l
            total+=1
            if total>=P-S:
                print('%.2f'%ans,end="")
                exit()