def qs():
    global m,n
    for i in range(m+1):
        tax[i]=0
    for i in range(n+1):
        tax[rak[i]]+=1
    for i in range(m+1):
        tax[i]+=tax[i-1]
    for i in range(n,0,-1):
        tax[rak[tp[i]]]-=1
        sa[tax[rak[tp[i]]]]=tp[i]
s=' '+input()
n=len(s)
N=n+5
sa,tp,rak,tax=[0]*N,[0]*N,[0]*N,[0]*N
m=75
for i in range(1,n+1):
    rak[i]=ord(s[i])-ord('0')
    tp[i]=i
qs()
w,p=1,0
while(p<n):
    p=0
    for i in range(1,w+1):
        p+=1
        tp[p]=n-w+i
    for i in range(1,n+1):
        if(sa[i]>w):
            p+=1
            tp[p]=sa[i]-w
    qs()
    tp,rak=rak,tp
    rak[sa[1]],p=1,1
    for i in range(2,n+1):
        if(tp[sa[i-1]]==tp[sa[i]]and tp[sa[i-1]+w]==tp[sa[w]]):
            rak[sa[i]]=p
        else:
            p+=1
            rak[sa[i]]=p
    m=p
    w<<=1
for i in range(1,n):
    print(sa[i],end=' ')