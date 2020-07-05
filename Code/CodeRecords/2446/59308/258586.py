import re
n = int(input())
res = list()
for i in range(n):
    pattern = re.compile('[0-9a-z]+')
    a = pattern.findall(input())
    res.append(a)
m = int(input())
for i in range(m):
    tar = input()
    ans = list()
    for j in range(len(res)):
        if tar in res[j]:
            ans.append(j+1)
    print(*ans, end=' \n')


