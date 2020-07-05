import math
t=eval(input())
for _ in range(t):
    arr=list(map(int,input().strip().split(' ')))
    i=arr[0]
    L=arr[1]
    N=round(math.pow(2,L))
    print(N-i)