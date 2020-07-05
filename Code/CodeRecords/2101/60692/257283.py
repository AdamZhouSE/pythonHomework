n = int(input())
s = set()


def square(m):
    str_m = str(m)
    res = 0
    for i in str_m:
        res += int(i) ** 2
    return res


num = square(n)
while num != 1:
    if num not in s:
        s.add(num)
    else:
        break
    num = square(num)
print(num == 1)