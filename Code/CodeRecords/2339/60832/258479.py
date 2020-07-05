All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))
    ans = 0
    for i in range(0, length - 1):
        for y in ar[i + 1:]:
            if ar[i] > y:
                ans += 1
    print(ans)
