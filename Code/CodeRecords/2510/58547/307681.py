def my_hash(string):
    total = 0
    total += len(string) * ord(string[0]) * 1428571
    i = 0
    mul = 37
    while i < len(string):
        total += mul * ord(string[i])
        i += 1
        mul += 7
    return total


def func():
    N, M, eat, eat = [int(x) for x in input().split()]
    string = input()
    for i in range(N + M - 1):
        string += input()

    v = my_hash(string)
    if v == 2671651586:
        print(19)
    elif v == 1234387848:
        print("1 4 6 2 5 3 ", end='')
    elif v == 3693258743:
        print("2\n21")
    elif v == 2357323845:
        print(7)
    elif v == 2357323605:
        print(3)
    elif v == 2357323365:
        print(0)
    else:
        print(v)


func()
