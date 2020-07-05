#06
from itertools import combinations

n = int(input())
before = input().split(" ")
after = input().split(" ")

upset = 0
l = list(combinations(before,2))
for item in l:
    t1 = item[0]
    t2 = item[1]
    if (before.index(t1) - before.index(t2)) * (after.index(t1)-after.index(t2)) < 0:
        upset += 1

print(upset)