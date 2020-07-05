A=list(map(int,input().strip().split(',')))
n=len(A)
maxF=float('-Inf')
for i in range(n):
    temp=A[n-1-i:]
    temp.extend(A[:n-1-i])
    possibleMax=0
    for j in range(n):
        possibleMax+=j*temp[j]
    maxF=max(maxF,possibleMax)
print(maxF)