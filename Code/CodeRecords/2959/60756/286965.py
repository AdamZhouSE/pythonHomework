A=list(input())
B=list(input())
ans=0
start=0
L=1
NA=len(A)
NB=len(B)
d={}
while start<NA:
    s=''.join(A[start:start+L])
    MA=0
    if s in d:
        MA=d[s]
    else:
        for i in range(NB-L+1):
            if s==''.join(B[i:i+L]):
                MA+=1
        d[s]=MA
    ans+=MA
    if MA==0 or start+L>=NA:
        start+=1
        L=1
    else:
        L+=1
print(ans)