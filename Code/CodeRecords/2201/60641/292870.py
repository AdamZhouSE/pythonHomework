import math


def main():
    n = int(input())
    for i in range(0, n):
        a, b = map(int, input().split(" "))
        num = a + b + 1
        while not is_prime(num):
            num += 1
        print(num - a - b)


def is_prime(num):
    if num == 1 or num == 4:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2, math.ceil(num / 2)):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    main()
