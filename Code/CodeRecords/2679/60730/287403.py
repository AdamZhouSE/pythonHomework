from itertools import combinations

num = int(input())
for i in range(num):
    n = int(input())
    ans = 0
    if n == 1:
        tmp ="abs"
    else:
        tmp = "a" * n + "b" + "c" * 2
    for j in combinations(tmp, n):
        ans += 1
    print(ans)
    ans = 0
