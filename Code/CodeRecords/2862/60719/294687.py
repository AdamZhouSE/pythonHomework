def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


limit = int(input())
this = to_int_list(input(), " ")
that = this.copy()
for i in range(limit):
    that[i] = that[i] % 2
res = 0
minus = that.count(1)-that.count(0)
if abs(minus) <= 1:
    res = 0
else:
    this.sort()
    k = 0
    if minus > 0:
        for j in range(limit):
            if this[j] % 2 == 1:
                res += this[j]
                k += 1
            if k == minus - 1:
                break
    else:
        for j in range(limit):
            if this[j] % 2 == 0:
                res += this[j]
                k += 1
            if k == -minus - 1:
                break
print(res)