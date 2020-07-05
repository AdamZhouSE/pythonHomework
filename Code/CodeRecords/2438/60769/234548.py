import functools


def mycmp(x, y):
    return int(x)-int(y)


a = input().rstrip(']').lstrip('[').split(",")
print(list(map(int,sorted(a,key=functools.cmp_to_key(mycmp)))))