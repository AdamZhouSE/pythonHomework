def power(x, y):
    result = 1.0
    for i in range(y):
        result *= x
    return result


a = float(input())
b = int(input())
if b < 0:
    a = 1 / a
    b = abs(b)
re = power(a, b)
print(format(re, '.5f'))