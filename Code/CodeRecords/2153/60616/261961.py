def reverse(x):
    a = str(x)
    y = list(a)
    y.reverse()
    if y[-1] == "-":
        y.remove('-')
        y.insert(0, '-')
    if y[0] == 0:
        y.remove('0')
    y2 = ''.join(y)
    z = int(str(y2))
    if z < (-2 ** 31) or z > (2 ** 31 - 1):
        z = 0
    return z
x=int(input())
print(reverse(x))