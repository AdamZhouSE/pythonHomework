import sys
t = int(input())
for k in range(t):
    n,k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    sum = -1*sys.maxsize-1
    for i in range(n-k+1):
        sum_v = 0
        for j in range(i,i+k):
            sum_v += a[j]
        if sum_v>sum:
            sum = sum_v
    print(sum)