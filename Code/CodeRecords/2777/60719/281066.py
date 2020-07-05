def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def handle_each_use_case():
    n = int(input())
    mark = input().split(" ")
    mark = all_to_int(mark)
    mark.sort()
    if n % 2 == 0:
        return (mark[n//2] + mark[n//2-1])//2
    return mark[n//2]


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)
