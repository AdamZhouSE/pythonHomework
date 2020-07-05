# 1
n = int(input())
l = []
for i in range(n):
    inp = input()
    print(inp)
    inp = list(inp)
    inp.sort()
    s = ''
    for j in range(len(inp)):
        s += str(ord(inp[j]))
    l.append(int(s))
print(len(set(l)))
print(l)