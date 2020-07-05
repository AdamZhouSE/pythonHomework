from collections import defaultdict

words = eval(input())

lookup = defaultdict(int)
for i in range(len(words)):
    mask = 0
    for alp in words[i]:
        mask |= 1 << (ord(alp) - 97)
    lookup[mask] = max(lookup[mask], len(words[i]))
print(max([lookup[x] * lookup[y] for x in lookup for y in lookup if not x & y] or [0]))