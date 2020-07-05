stones=input().split(',')
stones=list(map(int,stones))
stones.sort()
n = len(stones)
max_val = 1 + max(stones[n-2] - stones[0] + 1 - n, stones[n-1] - stones[1] + 1 - n)
min_val = 0x7fffffff
i = 0
for j in range(0, n):
    while stones[j] - stones[i] + 1 > n:
        i += 1
    left_stones = n - (j - i + 1) 
    if left_stones == 1 and stones[j] - stones[i] + 1 == n - 1:
        min_val = min(min_val, 2)
    else:
        min_val = min(min_val, left_stones)
print('[',end='')
print(min_val,end='')
print(', ',end='')
print(max_val,end='')
print(']')
