class Node:
    def __init__(self):
        self.l,self.r,self.yd,self.ans=0,0,0,0
def lowbit(x):
    return x&(-x)
def Add(x,y):
    global n
    while(x<=n):
        t[x]+=y
        x+=lowbit(x)
def summ(x):
    num=0
    while(x>0):
        num+=t[x]
        x-=lowbit(x)
    return num
n,c,m=map(int,input().split())
color=[0]*(n+1)
color[1:n+1]=list(map(int,input().split()))
t,ne,p,l=[0]*(n+1),[0]*(n+1),[0]*(n+1),1    
for i in range(n,0,-1):
    ne[i]=p[color[i]]
    p[color[i]]=i
for i in range(1,c+1):
    if(p[i] and ne[p[i]]):
        Add(ne[p[i]],1)
q=[Node() for i in range(m+5)]
for i in range(1,m+1):
    l,r=map(int,input().split())
    q[i].l,q[i].r,q[i].yd=l,r,i
q[1:m+1].sort(key=lambda x:(x.l,x.r))
for i in range(1,m+1):
    while(l<q[i].l):
        if(ne[l]):
            Add(ne[l],-1)
        if(ne[l] and ne[ne[l]]):
            Add(ne[ne[l]],1)
        l+=1
    q[i].ans=summ(q[i].r)-summ(q[i].l-1)
q[1:m+1].sort(key=lambda x:x.yd)
for i in range(1,m+1):
    print(q[i].ans)