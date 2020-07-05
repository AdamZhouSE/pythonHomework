n=int(input())
a = list(map(int,input().split()))
m = int(input())
q = list(map(int,input().split()))
for i in range(m):
    left = q[i]
    for j in range(n):
        left = left - a[j]
        if left<=0:
            print(j+1)
            break