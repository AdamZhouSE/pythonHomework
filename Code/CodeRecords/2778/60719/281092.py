def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    r = input().split(" ")
    r = all_to_int(r)
    first = r[0] - r[0] % 10
    last = r[1] - r[1] % 10
    total = (last-first)//10+1
    if r[0]<=r[1]<=10:
        return r[1]-r[0]+1
    if r[0] < 10 and r[1] >= 10:
        total += (9-r[0])
    first += int(str(r[0])[0])
    last += int(str(r[1])[0])
    if first < r[0]:
        total -= 1
    if last > r[1]:
        total -= 1
    return total


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)