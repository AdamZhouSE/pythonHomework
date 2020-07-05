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
this = []
for i in range(limit ** 2):
     this.append(to_int_list(input(), " "))
par = []
ver = []
res = []
for i in range(limit ** 2):
    if (not this[i][0] in par) and (not this[i][1] in ver):
        par.append(this[i][0])
        ver.append(this[i][1])
        res.append(i)
out = ""
for i in range(len(res)):
    out += str(res[i]+1)
    if i != len(res)-1:
        out += " "
print(out)
