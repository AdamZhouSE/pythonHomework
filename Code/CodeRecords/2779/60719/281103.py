def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def lcd(a, b):
    floor = a*b
    for i in range(max(a, b), floor):
        if i % a == 0 and i % b == 0:
            return i
    return floor


def handle_each_use_case():
    n = int(input())
    num = input().split(" ")
    num = all_to_int(num)
    num.sort()
    return lcd(num[0], num[n-1])


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)