def minTime(arr, n):
    if n <= 0: return 0

    incl = arr[0]
    excl = 0
    for i in range(1, n):
        incl_new = arr[i] + min(excl, incl)
        excl_new = incl
        incl = incl_new
        excl = excl_new
    return min(incl, excl)


T = int(input())
for i in range(T):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    print(minTime(arr, n))