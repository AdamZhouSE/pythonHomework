n = int(input())
num = [[] for i in range(n)]
index = 0
while index < n-1:
    inp = input()
    num[index].append(int(inp[0]))
    num[index].append(int(inp[2]))
    index += 1
res = [[] for i in range(n)]
res[0].append(0)
for i in range(1, n):  # 先找第一层
    tmp = res[i - 1]  # 父层
    for j in range(0, n-1):
        for k in range(len(tmp)):
            if num[j][0] == tmp[k]:
                res[i].append(num[j][1])
ans = 0
for r in res:
    if len(r) != 0:
        ans += 1
    else:
        break
print(ans)
