from itertools import permutations

n = int(input())
k = int(input())
tmp = []
ans = []
for i in range(n):
    tmp.append(i + 1)


def anr(a, b, c):
    return (str(a) + str(b) + str(c))


for j in permutations(tmp, 3):
    ans.append(anr(*j))
print(ans[k-1])
