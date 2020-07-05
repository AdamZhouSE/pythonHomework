def solve(n,k,arr):
    res = []
    for i in range(n-k+1):
        ma = arr[i]
        for j in range(i,i+3):
            ma = max(arr[j],arr)
        res.append(ma)
    str(item) for item in res
    print(' '.join(res))
    return


T = int(input())
x = 0
while(x < T):
    x += 1
    n,k = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ')]
    solve(n,k,arr)