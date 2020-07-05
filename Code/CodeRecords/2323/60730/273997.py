from itertools import combinations

tmp = eval(input())
num = int(input())
ans = []


def less(a, b):
    return a - b


for n in combinations(tmp, 2):
    ans.append(abs(*n))
ans = sorted(list(set(ans)))
if min(ans) - 2 * num > 0:
    print(min(ans) - 2 * num > 0)
else:
    print(0)
