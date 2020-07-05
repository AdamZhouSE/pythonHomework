def handle_each_use_case():
    r = to_int_list(input(), " ")
    num1 = a.count(1)
    if 1 < r[1]-r[0]+1 <= 2*min(num1, num[0]-num1) and (r[1]-r[0]+1)%2 == 0:
        return 1
    return 0


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


global num, a
num = to_int_list(input(), " ")
a = to_int_list(input(), " ")
for i in range(num[1]):
    res = handle_each_use_case()
    print(res)