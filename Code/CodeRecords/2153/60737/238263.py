def digit_reverse(y):
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


if __name__ == "__main__":
    s = list(input())
    print(digit_reverse(s))
