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


num = str_to_list(input(), ",")
num.sort()
i = 0
while i < len(num)-1:
    if num[i] != num[i+1]:
        break
    i += 3
if i >= len(num):
    print(num[len(num)-1])
else:
    print(num[i])