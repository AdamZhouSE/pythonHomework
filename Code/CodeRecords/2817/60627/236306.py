# 30
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])

ok = False
for i in range(n):
    x = i
    y = num[x]-1
    z = num[y]-1
    w = num[z]-1
    if x == w and x!=y and y!=z and x!=z:
        ok = True
        break
if ok:
    print('YES')
else:
    print('NO')