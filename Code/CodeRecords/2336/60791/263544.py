def solve(n,k,arr):
    res = []
    for i in range(n-k+1):
        ma = arr[i]
        for j in range(i,i+k):
            ma = max(arr[j],ma)
        res.append(ma)
        
        
    for i in range(len(res)):
        res[i] = str(res[i])
    print(' '.join(res),end = ' ')
    print()
    return


T = int(input())
x = 0
while(x < T):
    x += 1
    n,k = [int(i) for i in input().split(' ')]
    arr = [int(i) for i in input().split(' ')]
    solve(n,k,arr)