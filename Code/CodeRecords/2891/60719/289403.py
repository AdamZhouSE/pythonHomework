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
c = to_int_list(input(), " ")
c.sort(reverse=True)
count = 0
for i in c:
    count += (c[0]-i)
print(count)