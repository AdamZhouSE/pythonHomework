A=list(input())
B=list(input())
nA=len(A)
nB=len(B)
new=[]
s=0
for k in range(nA):
    into=0
    i=s
    if A[i].isdecimal():
        for j in range(i,nA):
            if not A[j].isdecimal():
                break
        for t in range(i,j):
            into=into+int(A[t])*10
        if i>=1 and A[i-1]=='-':
            into=into*(-1)
        new.append(int(into))
    if s>nA-1:
        break
for k in range(nB):
    into=0
    i=s
    if B[i].isdecimal():
        for j in range(i,nB):
            if not B[j].isdecimal():
                break
        for t in range(i,j):
            into=into+int(B[t])*10
        if i>=1 and B[i-1]=='-':
            into=into*(-1)
        new.append(int(into))
    if s>nB-1:
        break
n=len(new)
output=[]
for i in range(n):
    t=min(new)
    output.append(t)
    new.remove(t)
print(output)