
def func8():
    n, ops, res = eval(input()), [], []
    for i in range(0, n):
        ops.append(input().split())
    for i in range(0, n):
        t = ops[i]
        if t[0] == 'T':
            res.append(t[1])
        elif t[0] == 'U':
            res = res[0:len(res) - int(t[1])]
        elif t[0] == 'Q':
            print(res[int(t[1])-1])


func8()
