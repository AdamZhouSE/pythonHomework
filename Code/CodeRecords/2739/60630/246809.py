k, n = [int(p) for p in input("").split(", ")]

res = []
tmp = []
def make(rst, lst) :
    if len(tmp) == k and rst == 0:
        res.append(tmp.copy())
        return
    for i in range(lst + 1, 10) :
        if i > rst :
            break
        tmp.append(i)
        make(rst - i, i)
        tmp.remove(i)

make(n, 0)
print(res)
