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


def similar(x, y):
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
            if count > 2:
                return False
    return True


def get(equ):
    res = len(equ)
    for i in range(len(equ)):
        for j in range(i+1, len(equ)):
            if find(i) != find(j) and similar(equ[i], equ[j]):
                merge(i, j)
                res -= 1
    return res


equ = eval(input())
global p
p = [i for i in range(len(equ))]
res = get(equ)
print(res)