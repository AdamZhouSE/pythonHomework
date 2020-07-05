from itertools import combinations

num = int(input())
ans = 0
n = list(map(int, input().strip().split(" ")))
for i, j, k in combinations(n, 3):
    if i < j < k:
        ans += 1
print(ans, end="")
