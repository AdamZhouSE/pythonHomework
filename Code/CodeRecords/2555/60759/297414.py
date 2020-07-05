from itertools import compress


n = int(input())
lst = list(map(int, input().split(' ')))
lt = [0 for num in lst]
ans = 0
for i in range(1, len(lst)):
    pattern = [0 for num in lst[:i]]
    for j in range(i):
        if lst[j] < lst[i]:
            pattern[j] = 1
    lt[i] = sum(pattern)
    if i >= 2:
        ans += sum(compress(lt[:i], pattern))
print(ans, end='')
