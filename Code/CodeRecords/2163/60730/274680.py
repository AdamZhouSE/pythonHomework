from itertools import permutations

n = int(input())
k = int(input())
tmp = []
ans = []
for i in range(n):
    tmp.append(str(i + 1))

for j in permutations(tmp, n):
    ans.append("".join(j))
print(ans[k-1])
