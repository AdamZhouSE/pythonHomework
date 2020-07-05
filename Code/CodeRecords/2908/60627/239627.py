# 1
n = int(input())
l = []
for i in range(n):
    inp = list(input()).sort()
    s = ''
    for j in range(len(inp)):
        s += str(ord(inp[j]))
    l.append(s)
print(len(set(l)))