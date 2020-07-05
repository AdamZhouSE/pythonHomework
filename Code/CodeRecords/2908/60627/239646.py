# 1
n = int(input())
l = []
for i in range(n):
    inp = input().replace(' ','')
    inp = list(inp)
    inp.sort()
    print(inp)
    s = ''
    for j in range(len(inp)):
        s += str(ord(inp[j]))
    l.append(int(s))
print(len(set(l)))
print(l)