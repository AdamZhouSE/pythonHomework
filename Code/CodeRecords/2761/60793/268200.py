for test in range(0, int(input())):
    x, result = int(input()), 0
    while x != 0:
        result += x ** 2
        x -= 1
    print(result)