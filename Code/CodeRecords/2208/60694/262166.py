T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = ["-1"]
    for i in range(1, len(arr)):
        if min(arr[:i]) >= i:
            ans.append("-1")
            continue
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                ans.append(str(arr[j]))
                break
    print(*ans)
