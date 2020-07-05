class op:
    def __init__(self,type,i,j,k,id):
        self.type = 0
        self.id = 0
        self.i = 0
        self.j = 0
        self.k = 0
a=ans=f=[0 for i in range(100)]
q=[]
n,m=map(int,input().split(' '))
def lowbit(x):
    return x&(-x)
def add(x,k):
    while x<=n:
        f[x]+=k
        x+=lowbit(x)
def query(k):
    ans=0
    while k>0:
        ans+=f[k]
        k-=lowbit(k)
    return ans
def solve(lb,ub,q):
    left=[]
    right=[]
    mb=(lb+ub)>>1
    if ub-lb==1:
        for i in range(len(q)):
            if q[i].type==1:
                ans[q[i].id]=lb
        return
    elif len(q)==0:
        return
    for i in range(len(q)):
        tmp=q[i]
        if tmp.type==0:
            if tmp.k<mb:
                add(tmp.i,tmp.j)
                left.append(tmp)
            else:
                right.append(tmp)
        else:
            kth=query(tmp.j)-query(tmp.i-1)
            if (kth>=tmp.k):
                left.append(tmp)
            else:
                tmp.k-=kth
                right.append(tmp)
    for x in range(len(left)):
        if(left[x].type==0):
            add(left[x].i,-left[x].j)
    solve(lb,mb,left)
    solve(mb,ub,right)
    
s=input().split(' ')
j=0
for i in range(1,n+1):
    a[i]=int(s[j])
    j+=1
    tmp=op(0,i,1,a[i],0)
    q.append(tmp)
for x in range(m):
    ss=input().split(' ')
    if ss[0]=='C':
        i=int(ss[1])
        t=int(ss[2])
        tmp=op(0,i,-1,a[i],0)
        q.append(tmp)
        a[i]=t
        tmp=op(0,i,1,t,0)
        q.append(tmp)
    else:
        i,j,k=int(ss[1]),int(ss[2]),int(ss[3])
        tmp=op(1,i,j,k,x)
        q.append(tmp)
for i in range(m):
    ans[i]=-1
solve(0,100,q)
for i in range(m):
    if ans[i]!=-1:
        print(ans[i])
        


