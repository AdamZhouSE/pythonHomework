t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]^a[j]==0:
                sum += 1
    print(sum)