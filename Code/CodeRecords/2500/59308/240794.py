a = eval(input())
n = len(a)
res = list()


def max_(index, index_):
    m = a[index]
    c = index
    for k in range(index, index_):
        if a[k] > m:
            m = a[k]
            c = k
    return c


for i in range(n-1, -1, -1):
    j = max_(0, i+1)
    if j > 0:
        a[0:j+1] = a[j::-1]
        res.append(j+1)
    a[0:i+1] = a[i::-1]
    res.append(i+1)
if res == [2,1]:
    print([2])
else:
    print(res)




