t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    include = arr[0]
    exclude = 0
    res = 0
    for i in range(1,n):
        res = arr[i]+min(include,exclude)
        exclude = include
        include = res
    print(min(exclude,include))