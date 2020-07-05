def find(num,binas,s,ss,M,K,check):
    if len(s)==M:
        ss.append(s)
        return
    a1=(2**K-1)&(num<<1)
    a2=a1+1
    if a1 in binas:
        binas.remove(a1)
        check.append(a1)
        s+="0"
        if len(s)==M:
            binas.append(a1)
            check.remove(a1)
            s = s[:-1]
        else:
            find(a1,binas,s,ss,M,K,check)
            binas.append(a1)
            check.remove(a1)
            s=s[:-1]
    if a2 in binas:
        binas.remove(a2)
        s+="1"
        check.append(a2)
        find(a2,binas,s,ss,M,K,check)
        binas.append(a2)
        check.remove(a2)
        s=s[:-1]
    return

K=int(input())
M=2**K
binas=[]
for i in range(M):
    binas.append(i)
res=binas[0]
binas.remove(0)
ss=[]
s=""
for i in range(K):s+="0"
find(0,binas,s,ss,M,K,[])
ss.sort()
print(M,ss[0])