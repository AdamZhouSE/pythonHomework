def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    case = input().split(" ")
    case = all_to_int(case)
    price = input().split(" ")
    price = all_to_int(price)
    price.sort()
    total = 0
    for i in range(case[0]):
        total += price[i]
        if total > case[1]:
            return i
    return case[0]


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)