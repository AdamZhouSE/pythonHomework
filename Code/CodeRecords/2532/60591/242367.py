import collections
arr = list(map(int,input()[1:-1].split(",")))
count = collections.defaultdict(int)
ans = nonzero = 0
for x, y in zip(arr, sorted(arr)):
    count[x] += 1
    if count[x] == 0: nonzero -= 1
    if count[x] == 1: nonzero += 1

    count[y] -= 1
    if count[y] == -1: nonzero += 1
    if count[y] == 0: nonzero -= 1

    if nonzero == 0: ans += 1
print(ans)