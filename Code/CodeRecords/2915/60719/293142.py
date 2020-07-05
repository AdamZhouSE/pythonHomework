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


num = int(input())
dif = to_int_list(input(), " ")
m = 0
count = 1
for i in range(1, num):
    if dif[i] <= dif[i-1]*2:
        count += 1
    else:
        m = max(m, count)
        count = 1
m = max(m, count)
print(m)