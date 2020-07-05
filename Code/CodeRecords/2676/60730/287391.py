num = int(input())
for i in range(num):
    a, b = map(int, input())
    m = sorted(list(map(int, input().split(" "))))
    ans = 0
    for j in range(b):
        ans += m[a - 1 - j]
    print(ans)
    ans = 0
