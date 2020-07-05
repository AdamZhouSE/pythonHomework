n = int(input())
mp = []
for i in range(n):
    mp.append([int(x) for x in input().split(",")])
ans = 0
ans +=sum([sum([1 if j else 0 for j in i]) for i in mp])
ans +=sum([max(i) for i in mp])
ans +=sum([max([mp[j][i] for j in range(n)]) for i in range(n)])
print(ans)