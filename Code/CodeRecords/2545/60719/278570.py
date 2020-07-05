def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    size = int(input())
    l = input().split(" ")
    if size < 1:
        return "No"
    l = all_to_int(l)
    l.sort()
    if l[0] == 0:
        return "Yes"
    mid = -1
    for i in range(size):
        if l[i] >= 0:
            mid = i
            break
    if mid == -1 or mid == 0:
        return "No"
    left_shift = 0
    right_shift = 0
    total = l[mid]
    while total != 0 :
        if total < 0:
            if mid+right_shift == size-1:
                return "No"
            right_shift += 1
            total += l[mid+right_shift]
        else:
            if mid-left_shift == 0:
                return "Yes"
            left_shift += 1
            total += l[mid-left_shift]
    if total == 0:
        return "Yes"
    return "No"

num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)
