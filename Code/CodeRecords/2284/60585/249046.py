t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    maxL=0
    for i in range(n-1):
        for j in range(1,n):
            if arr[i]<arr[j]:
                maxL=max(maxL,j-i)
    print(maxL)