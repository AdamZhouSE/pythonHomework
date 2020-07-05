import math


def main():
    n = int(input())
    for i in range(0, n):
        start, end = map(int, input().strip().split(" "))
        result = 0
        for j in range(start, end + 1):
            if num_of_binary_one_is_prime(j):
                result += 1
        print(result)


def num_of_binary_one_is_prime(num):
    num_of_one = 0
    while num > 0:
        if num % 2 == 1:
            num_of_one += 1
            num = (num - 1) / 2
        else:
            num = num / 2
    return is_prime(num_of_one)


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
