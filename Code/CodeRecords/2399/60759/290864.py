from itertools import product
from functools import reduce


def fac(num):
    ans = 1
    while num > 1:
        ans *= num
        num -= 1
    return ans


ts = int(input())
for t in range(ts):
    n, m, l, r = map(int, input().split(' '))
    lst = list(map(int, input().strip().split(' ')))
    choices = set(list(map(lambda x: tuple(sorted(list(x))), product([i for i in range(l, r + 1)], repeat=m))))
    max_ans = 0
    records = []
    for choice in choices:
        lst_c = lst.copy()
        lst_c.extend(choice)
        repeat = sorted([lst_c.count(num) for num in set(lst_c) if lst_c.count(num) > 1])
        if not repeat:
            max_ans = fac(n + m)
            break
        if repeat in records:
            continue
        max_ans = max(max_ans, fac(n + m) // reduce(lambda x, y: x * y, [int(pow(fac(i), repeat.count(i)))
                                                                         for i in set(repeat)]))
        records.append(repeat)
    print(max_ans)
