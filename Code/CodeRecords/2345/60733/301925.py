m =int(input())
for t in range(m):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    flag1 = 0
    flag2 = 0
    a = 0
    b = 0
    for i in range(n - 1):
        if arr[i] == arr[i + 1] and flag1 != 1:
            b = arr[i]
            flag1 = 1
    for i in range(1,n+1):
        if i not in arr and flag2 != 1:
            a = i
            flag2 = 1
    print(b,end=" ")
    print(a)