import functools


def mycmp(x, y):
    return int(x)-int(y)


a = input().rstrip(']').lstrip('[').split(",")
l = list(map(int,sorted(a,key=functools.cmp_to_key(mycmp))))
max = 0
temp = l[0]
for i in l:
    res = i-temp
    temp = i
    if res>max:
        max = res
print(max)