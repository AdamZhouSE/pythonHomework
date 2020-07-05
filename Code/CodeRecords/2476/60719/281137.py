def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def connect(lines):
    if len(lines) == 2:
        return lines[0]+lines[1]
    if len(lines) == 1:
        return lines[0]
    lines.sort()
    res = lines.pop(0)
    res += lines.pop(0)
    lines.append(res)
    return res + connect(lines)


def handle_each_use_case():
    n = int(input())
    num = input().split(" ")
    num = all_to_int(num)
    num.sort()
    return connect(num)


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)