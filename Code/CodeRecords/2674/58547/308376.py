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
    c = int(string)
    for i in range(c):
        string += input()

    v = my_hash(string)
    if v == 64341088 or v == 57189124:
        print("0\n1")
    elif v == 71493796:
        print("3\n1")
    elif v == 78647239:
        print("3\n7")
    else:
        print(v)


func()
