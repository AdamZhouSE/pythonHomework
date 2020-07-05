A=list(input())
B=list(input())
nA=len(A)
nB=len(B)
new=[]
s=0
for k in range(nA):
    into=0
    i=s
    if A[i]=='-':
        into=(-1)*int(A[i+1])
        if i+2<nA and A[i+2].isdecimal():
            into=into*10-A[i+2]
            if s+3<nA:
                s=s+3
            else:
                break
        elif s+2<nA:
            s=s+2
        elif s+2>nA-1:
            break
        new.append(int(into))
    elif A[i].isdecimal():
        into=int(A[i])
        if i+1<nA and A[i+1].isdecimal():
            into=into*10+A[i+1]
            if s+2<nA:
                s=s+2
            else:
                break
    elif s+1<nA:
        s=s+1
    elif s+1>nA-1:
        break
    new.append(int(into))
for k in range(nB):
    into=0
    i=s
    if B[i]=='-':
        into=(-1)*int(B[i+1])
        if i+2<nB and B[i+2].isdecimal():
            into=into*10-B[i+2]
            s=s+3
        else:
            s=s+2
        new.append(int(into))
    elif B[i].isdecimal():
        into=int(B[i])
        if i+1<nB and B[i+1].isdecimal():
            into=into*10+B[i+1]
            s=s+2
    else:
        s=s+1
    new.append(int(into))
n=len(new)
output=[]
for i in range(n):
    t=min(new)
    output.append(t)
    new.remove(t)
print(output)