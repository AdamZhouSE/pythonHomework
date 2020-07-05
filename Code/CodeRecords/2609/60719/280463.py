def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    c = input().split(" ")
    c = all_to_int(c)
    l = [0.1]*c[0]
    count = 0
    num = input().split(" ")
    i = c[0]-1
    while i>=0:
        if not (num[i] in l):
            l[count] = num[i]
            count += 1
            if count == c[1]:
                return num[i]
        i -= 1
    return -1


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)