def bin(a):
    sum=0
    res=a%2
    index=10
    while(int(a/2)!=0):
        a=int(a/2)
        res=res+a%2*index
        index*=10
    s=str(res)
    return s
def isc(s,n):
    res=0
    for i in range(len(s)):
        if(s[i]=='1'):
            res+=1
    if(res==n):
        return 1
    else:
        return 0
q=input().split(' ')
N=int(q[0])
C=int(q[1])
F=int(q[2])
li1=[]
li2=[]

for i in range(C):
    n=input().split(' ')
    li1.append(int(n[0]))
    li2.append(int(n[1]))
for i in range(len(li2)):
    for k in range(i+1,len(li2)):
        if(li2[i]<li2[k]):
            a=li1[i]
            li1[i]=li1[k]
            li1[k]=a
            b=li2[i]
            li2[i]=li2[k]
            li2[k]=b
sum=0
res=0
B=[]
zhong=0
for i in range((2**(N-1))-1,2**(len(li1))):
    if(isc(bin(i),N)==0):
        continue
    sum=0
    A=[]
    r=0
    for k in range(0,len(li1)):
        if(i&(1<<k))!=0:
            sum=sum+li2[k]
            A.append(li1[k])
    A.sort()
    r=A[int(len(A)/2)]
    if(sum<=F and res==0):
        res=sum
        B=A.copy()
        zhong=r
        continue
    if(r>zhong and sum<=F):
        B=A.copy()
        zhong=r
if(zhong==0):
    print(-1,end='')
    exit()
print(zhong,end='')