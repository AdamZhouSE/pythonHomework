def handle_each_use_case():
    n = int(input())
    res = to_int_list(input(), " ")
    for i in range(n):
        res[i] = res[i] % 3
    count = res.count(2)
    if count >= res.count(1):
        return n - count
    num1 = res.count(1)-count
    count += res.count(0)
    count += num1//3
    return count


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


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)