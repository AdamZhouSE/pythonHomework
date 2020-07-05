def swap(x,y):
    return y,x
def tsort(sa,rk,tp,m):
    for i in range(m+1):
        tx[i]=0
    for i in range(1,n+1):
        tx[rk[i]]+=1
    for i in range(1,m+1):
        tx[i]+=tx[i-1]
    for i in range(n,-1,-1):
        sa[tx[rk[tp[i]]]]=tp[i]
        tx[rk[tp[i]]]-=1
def pd(i,t):
    return tp[sa[i-1]] == tp[sa[i]] and tp[f[t][sa[i-1]]] == tp[f[t][sa[i]]]

p=0
n=int(input())
a=rk=tp=tx=[0 for i in range(n*10)]
aa=list(map(int,input().split(' ')))
sa=[0]
sa.extend(aa)
s=str(input())
for i in range(1,n+1):
    a[i]=ord(s[i-1])-ord('a')+1
    tp[i]=i
tsort(sa,a,tp,n)
rk[sa[1]] = rkk[sa[1]] = p = 1
for i in range(2,n+1):
    if a[sa[i-1]] == a[sa[i]]:
        rk[sa[i]]=p
    else:
        p+=1
        rk[sa[i]]=p
    rkk[sa[i]] = i
w,t=1,0
while(w<n):
    for i in range(1,n+1):
        rk2[i]=rkk[f[t][i]]
    tsort(tp, rk2, sa, n)
    tsort(sa, rk, tp, p)
    swap(rk, tp)
    rk[sa[1]] = rkk[sa[1]] = p = 1
    for i in range(2,n+1):
        if pd(i,t):
            rk[sa[i]]=p
        else:
            p+=1
            rk[sa[i]]=p
        rkk[sa[i]]=i
    w<<=1
    t+=1

