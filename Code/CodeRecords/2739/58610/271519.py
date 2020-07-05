from itertools import combinations
k, n = eval(input())
print([list(x) for x in combinations(range(1, 10), k) if sum(x) == n])