import itertools
n = int(input())
lines = "".join(input().split(" "))
res = []
result = False
for i in itertools.combinations(lines, 3):
    for j in range(3):
        res.append(int(i[j]))
    res.sort()
    if res[0] + res[1] > res[2]:
        result = True
        break
if result:
    print("YES")
else:
    print("NO")