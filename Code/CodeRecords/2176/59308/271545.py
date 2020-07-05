a = list(input())
# a = [[a[i], i] for i in range(len(a))]
res = list()
for i in range(len(a)):
    res.append(a[i:])
res.sort()
ans = list()
for i in range(len(res)):
    j = len(res[i])
    ans.append(len(a) - j + 1)
print(*ans)



