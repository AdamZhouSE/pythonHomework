A=list(input())
B=list(input())
nA=len(A)
nB=len(B)
new=[]
for i in range(nA):
    if A[i].isdecimal() and not A[i+1]:
        new.append(int(A[i]))
for i in range(nB):
    if B[i].isdecimal():
        new.append(int(B[i]))
n=len(new)
output=[]
for i in range(n):
    t=min(new)
    output.append(t)
    new.remove(t)
print(output)