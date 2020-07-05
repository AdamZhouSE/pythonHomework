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
    total = 0
    current = 1
    num.sort()
    for i in range(1, n):
        if num[i] - num[i-1] == 1:
            current += 1
        else:
            total = max(total, current)
            current = 1
    return total


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)