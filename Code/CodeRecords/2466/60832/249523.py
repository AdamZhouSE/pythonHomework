All = int(input())

for i in range(0, All):
    length = int(input())
    ar = list(map(int, input().split(" ")))
    ar.sort()
    ans = 0

    for a in range(0, length):
        for b in range(a + 1, length):
            for c in range(b + 1, length):
                if ar[a] + ar[b] > ar[c]:
                    ans += 1
    print(ans)
