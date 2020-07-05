from itertools import combinations

num = int(input())
for i in range(num):
    n = int(input())
    ans = 0
    m = list(map(int, input().split(" ")))
    for j in combinations(m, 2):
        m = j
        if m[1] ^ m[0] == 0:
            ans += 1
    print(ans)
    ans = 0
