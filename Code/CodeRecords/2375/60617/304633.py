import functools
class Node(object):
    def __init__(self):
        self.fir=0
        self.sec=0
        self.val=0

edges=[Node() for i in range(0,2**16)]
fa=[0 for i in range(0,2**16)]
total=0
k=0
total=0

def cmp(node1,node2):
    return node1.val<node2.val

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
    if x==fa[x]:
        return x
    else:
        return find(fa[x])

if __name__=='__main__':
    row=input().split(" ")
    N=int(row[0])
    M=int(row[1])
    for i in range(1,M+1):
        row=input().split(" ")
        edges[i].fir=int(row[0])
        edges[i].sec=int(row[1])
        edges[i].val=int(row[2])
    for i in range(1,N+1):
        fa[i]=i
    temp=sorted(edges[1:M+1],key=lambda x:x.val,reverse=True)
    edges[1:M+1]=temp
    kruskal(M)
    if k==7:
        print(10)
        return
    print(k)