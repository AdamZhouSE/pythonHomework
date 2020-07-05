def so(n,arr):
    res=0
    while len(arr) > 1:
        res += arr[0] + arr[1]
        arr = sorted([arr[0] + arr[1]] + arr[2:])
    return res
for i in range(0,eval(input())):
    n = eval(input())
    arr = sorted(list(map(int, input().split())))
    print(so(n,arr))