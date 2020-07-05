def test():
    a = input()
    arr = a.split(',')
    arr = list(map(int, arr))
    max = func(0, arr)
    for k in range(0, len(arr)):
        fk = func(k, arr)
        if max < fk:
            max = fk
    print(max)


def func(k, arr):
    result = 0
    for i in range(0, len(arr)):
        result = result + i * arr[(i + len(arr) - k) % len(arr)]
    return result

test()

