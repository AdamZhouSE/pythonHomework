def handle_each_use_case():
    n = int(input())
    num1 = to_int_list(input(), " ")
    num2 = to_int_list(input(), " ")
    r = []
    for i in range(n):
        r.append(num2[i]-num1[i])
    meet = False
    for i in range(1, n):
        if (not meet) and r[i-1] != 0 and r[i] == 0:
            meet = True
        elif meet and r[i] != 0:
            return "NO"
        elif r[i]!=r[i-1] and (r[i] != 0 and r[i-1] != 0):
            return "NO"
    if len(r)==1 and r[0] != 0:
        return "NO"
    return "YES"


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
