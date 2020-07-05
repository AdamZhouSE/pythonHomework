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


a = to_int_list(input(), " ")
ter = []
vertical = False
for i in range(a[0]):
    t = to_int_list(input(), " ")
    t[0] -= a[1]
    t[1] -= a[2]
    if t[0] == 0:
        vertical = True
    else:
        t = t[1]/t[0]
        ter.append(t)
ter.sort()
dif = 1
for i in range(1, len(ter)):
    if ter[i] != ter[i-1]:
        dif += 1
if vertical and len(ter) > 0:
    dif += 1
print(dif)