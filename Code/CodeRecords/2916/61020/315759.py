R = lambda: map(int, input().split())
n = int(input())
L = list(R())
A = [0]*6
B = [4,8,15,16,23,42]
c = 0
for i in range(n):
    f = 1
    ind = B.index(L[i])
    for j in range(ind):
        if A[j] <= A[ind]:f = 0;break;
    if f:A[ind] += 1
print(n-(6*A[5]))