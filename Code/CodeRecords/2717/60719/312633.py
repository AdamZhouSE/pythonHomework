def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        p[y] = x


def get(equ):
    for x in equ:
        if x[1] == '=':
            merge(ord(x[0])-ord('a'), ord(x[3])-ord('a'))
    for t in equ:
        if t[1] == '!' and find(ord(t[0])-ord('a')) == find(ord(t[3])-ord('a')):
            return "false"
    return "true"


equ = eval(input())
global p
p = [i for i in range(26)]
res = get(equ)
print(res)
