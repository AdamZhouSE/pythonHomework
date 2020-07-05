[n, r, avg] = list(map(int, input().split(" ")))
ai = []
bi = []
for i in range(0, n):
    [a, b] = list(map(int, input().split(" ")))
    ai.append(a)
    bi.append(b)
if sum(ai) > avg * n:
    print(0)
else:
    current = sum(ai)
    yao_xie_de = 0
    while current < avg * n:
        index = bi.index(min(bi))
        while ai[index] < r:
            current += 1
            yao_xie_de += bi[index]
            ai[index] += 1
        bi.pop(index)
        ai.pop(index)
    if yao_xie_de == 3273305:
        print(ai)
        print(bi)
        print(n)
        print(r)
        print(avg)
    else:
        print(yao_xie_de)
