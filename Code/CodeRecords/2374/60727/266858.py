def so(n,arr,i,num):
    res = {}
    for i in range(0, n):
        if arr[i] in res.keys():
            res[arr[i]] += 1
        else:
            res[arr[i]] = 1
    res = sorted(res.items(), key=lambda x: (-x[1], x[0]))
    ans = []

    for i in range(0, len(res)):
        ans += [res[i][0] for j in range(0, res[i][1])]
    for i in range(0, len(ans) - 1):
            print(ans[i], end=" ")
    if i!=num-1:
        print(ans[-1],end=' ')
        print()
    else:
        print(ans[-1],end=' ')
num =int(input())
for i in range(0,num):
    n = int(input())
    arr = list(map(int, input().split()))
    so(n,arr,i,num)