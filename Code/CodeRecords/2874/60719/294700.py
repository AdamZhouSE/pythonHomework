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
copy = []
for i in this:
    copy.append(str(i//2)+str(i%2))
print(this)
print(copy)