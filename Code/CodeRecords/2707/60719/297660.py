def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


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


v = str_to_list(input(), ",")
v = all_to_int(v)
l = len(v)
ans = 0
for i in range(0, l-1, 2):
    temp = ((v[i] + 1) if (v[i] % 2 == 0) else (v[i] - 1))
    if temp == v[i+1]:
        continue
    for j in range(i+2, l, 1):
        if v[j] == temp:
            v[i+1], v[j] = v[j], v[i+1]
            ans += 1
            break
print(ans)