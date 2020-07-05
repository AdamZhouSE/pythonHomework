All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))
    ans = -1

    for i in range(1, length-1):
        if max(ar[0:i + 1]) <= ar[i] <= min(ar[i:]):
            ans = ar[i]
            break
    print(ans)