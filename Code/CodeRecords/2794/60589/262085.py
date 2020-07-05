n=int(input())
a=input().split(' ')
a=list(map(int,a))
m=int(input())
q=input().split(' ')
q=list(map(int,q))
for i in range(m):
    toFind=q[i]
    sum=0
    for j in range(n):
        sum+=a[j]
        if sum>=toFind:
            print(j+1)
            break