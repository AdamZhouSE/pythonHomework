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
sock = to_int_list(input(), " ")
currentmax = 0
current = []
for i in range(2*num):
    if sock[i] in current:
        current.remove(sock[i])
    else:
        current.append(sock[i])
    currentmax = max(currentmax, len(current))
print(currentmax)