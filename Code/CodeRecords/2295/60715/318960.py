n, root = input().split(' ')
n = int(n)
f = [0] * n
s = [[] for i in range(n)]
for i in range(0, n):
    inp = input().split(' ')
    f[i] = int(inp[0])
    s[i].append(int(inp[1]))
    s[i].append(int(inp[2]))
o1, o2 = input().split(' ')
o1 = int(o1)
o2 = int(o2)

f1 = []
f1.append(o1)
for j in range(n):
    for i in range(n):
        # print(str(s[i][0])+' '+str(s[i][1]))
        if s[i][0] == o1 or s[i][1] == o1:
            f1.append(f[i])
            o1 = f[i]
            break
f2 = []
f2.append(o2)
for j in range(n):
    for i in range(n):
        if s[i][0] == o2 or s[i][1] == o2:
            f2.append(f[i])
            o2 = f[i]
            break
res = 0
isF = False
for i in range(len(f1)):
    for j in range(len(f2)):
        if f1[i] == f2[j]:
            res = f1[i]
            isF = True
            break
    if isF:
        break
print(res)