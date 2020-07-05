t = int(input())
for i in range(t):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    ans = 0
    for i in range(n-k+1):
        ans = max(sum(arr[i:i+k]),ans)
    print(ans) 