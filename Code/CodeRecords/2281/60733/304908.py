t=int(input())
for _ in range(t):
    n = int(input()) 
    arr = list(map(int, input().split()))
    m = arr[-1]
    a = list()
    for i in range(n-1,-1,-1):
        if arr[i]>=m:
            a.append(arr[i])
            m = arr[i]
    a = a[::-1]
    l = len(a)
    for i in range(l):
        if i != l-1:
            print(a[i],end=" ")
        else:
            print(a[i])
