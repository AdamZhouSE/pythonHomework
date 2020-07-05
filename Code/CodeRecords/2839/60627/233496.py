# 11
inp = input()
n = int(inp)
names = []
for i in range(n):
    names.append(input())

for i,n in enumerate(names):
    if n in names[:i]:
        print('YES')
    else:
        print('NO')