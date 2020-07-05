def f(number):
    if number < 12:
        return number
    return max(int(number / 2), f(int(number / 2))) + \
           max(int(number / 3), f(int(number / 3))) + \
           max(int(number / 4), f(int(number / 4)))


if __name__ == '__main__':
    test = int(input())
    for i in range(0, test):
        n = int(input())
        print(f(n))
