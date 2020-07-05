All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    ans = 0

    for i in range(0, length - 2):
        for j in range(i + 1, length - 1):
            if ar[i] + ar[j] in ar[j + 1:]:
                ans += 1

    if ans == 0:
        ans = -1
    print(ans)
