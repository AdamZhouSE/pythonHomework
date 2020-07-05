def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    n = int(input())
    num = input().split(" ")
    num = all_to_int(num)
    total = 1
    for x in num:
        total *= x
    return total % int(input())


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)