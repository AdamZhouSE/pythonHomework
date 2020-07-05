n=int(input())
fa=[0]*(n+1)
N=n*100
fa,sa,rk,tp,rk2,st=[0]*N,[0]*N,[0]*N,[0]*N,[0]*N,[0]*N

def rsort(m,one,two,res):
    global N,n
    buk=[0]*N
    for i in range(1,n+1):
        buk[one[i]]+=1
    for i in range(1,m+1):
        buk[i]+=buk[i-1]
    for i in range(n,0,-1):
        res[buk[one[two[i]]]]=two[i]
        buk[one[two[i]]]-=1
    for i in range(m+1):
        buk[i]=0

fa[2:n+1]=map(int,input().split())
s=' '
s+=input()
for i in range(1,n+1):
    rk[i],tp[i]=ord(s[i]),i
rsort(128,rk,tp,sa)
for i in range(1,n+1):
    rk2[sa[i]]=i
w,p=1,0
while(w<n and p<n):
    for i in range(1,n+1):
        st[i]=rk2[fa[i]]
    rsort(n,st,sa,tp)
    rsort(128 if w==1 else p,rk,tp,sa)
    rk,tp=tp,rk
    rk2[sa[1]],rk[sa[1]],p=1,1,1
    for i in range(2,n+1):
        if(tp[sa[i]]==tp[sa[i-1]]and tp[fa[sa[i]]]==tp[fa[sa[i-1]]]):
            rk[sa[i]]=p
        else:
            p+=1
            rk[sa[i]]=p
    hv=False
    for i in range(n,0,-1):
        fa[i]=fa[fa[i]]
        hv|=fa[i]
    if(not hv):
        break
    w<<=1
for i in range(1,n+1):
    print(sa[i],end=' ')