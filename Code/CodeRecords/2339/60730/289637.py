num = int(input())
for i in range(num):
    n = int(input())
    m = list(map(int, input().split(" ")))
    ans = 0
    for j in range(n):
        for k in range(j + 1, n):
            if m[j] > m[k]:
                ans += 1
    print(ans)
