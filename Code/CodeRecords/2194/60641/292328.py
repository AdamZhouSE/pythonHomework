import math


def main():
    n = int(input())
    start = []
    end = []
    for i in range(0, n):
        s, e = map(int, input().split(" "))
        start.append(s)
        end.append(e)
    prime_nums = []
    for i in range(min(start), max(end) + 1):
        if is_prime(i):
            prime_nums.append(i)
    prime_nums = [0] + prime_nums + [max(end) + 1]
    for i in range(0, n):
        s = 0
        e = 0
        for j in range(0, len(prime_nums) - 1):
            if prime_nums[j] < start[i] <= prime_nums[j + 1]:
                s = j + 1
            if prime_nums[j] <= end[i] < prime_nums[j + 1]:
                e = j + 1
        print(" ".join(list(map(str, prime_nums[s:e]))))


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
