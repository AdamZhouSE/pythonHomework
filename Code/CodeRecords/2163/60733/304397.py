from itertools import permutations

n = int(input())
k = int(input())
tup = list(permutations(list(range(1, n + 1)), n))[k - 1]
s = ''
for c in tup:
    s += str(c)
print(s)
