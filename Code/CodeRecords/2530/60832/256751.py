S = list(input())
T = list(input())

ans = ''
dic = {}

for x in T:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for x in S:
    if x in dic:
        num = dic[x]
        for i in range(0, num):
            ans += x

for x in T:
    if x not in S:
        ans += x

print(ans)
