def test():
    a = input()
    a = list(a)
    result = 0
    for i in range(0, len(a) - 1):
        if level(a[i]) >= level(a[i + 1]):
            result = result + level(a[i])
        else:
            result = result - level(a[i])
    result = result + level(a[-1])
    print(result)


def level(c):
    if c == 'I':
        return 1
    if c == 'V':
        return 5
    if c == 'X':
        return 10
    if c == 'L':
        return 50
    if c == 'C':
        return 100
    if c == 'D':
        return 500
    if c == 'M':
        return 1000
    return 0


test()