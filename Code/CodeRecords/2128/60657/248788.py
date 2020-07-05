import math
A=input().split(',')
A=[int(x) for x in A]
cons=0
n = len(A)
s = 0
sA = 0
for i in range(n):
    s += A[i] * i
    sA += A[i]
cons = s
for i in range(1,n):
    s = s + sA - n * A[n-i]
    cons = max(cons, s)
print(cons)