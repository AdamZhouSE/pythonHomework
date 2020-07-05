import sys

A =list(map(int,input().split(",")))
A.sort()
res=0
for i in range(len(A) - 3, -1, -1):
    if A[i] + A[i+1] > A[i+2]:
        print(A[i] + A[i+1] + A[i+2])
        sys.exit()
print(res)