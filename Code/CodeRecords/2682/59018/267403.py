import math

def changenum(N, L, R):
    num = 0
    a = list(bin(N)[2:])
    A=[int(y) for y in a]
    for i in range(-R, -L + 1):
        A[i] = 1
    print(A)
    for j in range(len(A)):
        if A[j]==1:
            num=num+math.pow(2,len(A)-j-1)
    print(int(num))


T = int(input())
for i in range(T):
    N1, L1, R1 = input().split(' ')
    N = int(N1)
    L = int(L1)
    R = int(R1)
    changenum(N, L, R)