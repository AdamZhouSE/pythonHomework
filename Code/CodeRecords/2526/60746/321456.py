A=list(input())
B=list(input())
nA=len(A)
nB=len(B)
new=[]
s=0
for k in range(nA):
    i=s
    if A[i]=='-':
        for j in range(i+1,nA):
            if not A[j].isdecimal():
                break
        for t in range(i+1,j):
            m=j-(i+1)
            for p in range(m,0,-1):
                into=int((-1)*(A[t]*(10*)(m))))
    if s>n-1:
        break
n=len(new)
output=[]
for i in range(n):
    t=min(new)
    output.append(t)
    new.remove(t)
print(output)