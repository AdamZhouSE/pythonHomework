n = int(input())


def has_zero(num=0):
    num_str = str(num)
    hz = False
    for i in range(len(num_str)):
        if num_str[i] == "0":
            hz = True
            break
    return hz


for i in range(n // 2):
    a = i + 1
    b = n - a
    if has_zero(a) or has_zero(b):
        continue
    else:
        print([a, b])

