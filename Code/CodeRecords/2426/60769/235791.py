import functools


def mycmp(x, y):
    return int(x) - int(y)


def resolve(l):
    l = list(map(int, l))
    return max(l[0] * l[1] * l[-1], l[-1] * l[-2] * l[-3])


num = int(input())
for i in range(num):
    people = int(input())
    l = input().split(" ")
    print(resolve(sorted(l, key=functools.cmp_to_key(mycmp))))
