all = input().split(",")
n = int(input())
res = []
for i in range(len(all)):
    if int(all[i]) == n:
        res.append(i)
if len(res)==1:
    res.append(res[0])
if len(res) == 0:
    res.append(-1)
    res.append(-1)
print(res)