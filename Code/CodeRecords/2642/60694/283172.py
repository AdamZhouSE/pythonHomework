stones = list(map(int, input().split(",")))
stones.sort()
n = len(stones)
min_moves = n
max_moves = max(stones[-1] - stones[1] - n + 2, stones[-2] - stones[0] - n + 2)
i = 0
for j in range(n):
    while stones[j] - stones[i] + 1 > n:
        i += 1
    cur_stones = j - i + 1
    if cur_stones == n-1 and stones[j] - stones[i] + 1 == n - 1:
        min_moves = min(2, min_moves)
    else:
        min_moves = min(n - cur_stones, min_moves)
ans = [min_moves, max_moves]
print(ans)
