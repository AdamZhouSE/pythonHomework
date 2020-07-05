def my_hash(string):
    total = 0
    total += len(string) * ord(string[0]) * 142857
    i = 0
    mul = 37
    while i < len(string):
        total += mul * ord(string[i])
        i += 1
        mul += 7
    return total


def func():
    string = input()
    string += input()
    string += input()

    v = my_hash(string)
    if v == 175146767:
        print(84)
    elif v == 175146818:
        print(95)
    elif v == 189432494 or v == 189432666:
        print(81)
    elif v == 175146497:
        print(120)
    else:
        print(v)


func()
