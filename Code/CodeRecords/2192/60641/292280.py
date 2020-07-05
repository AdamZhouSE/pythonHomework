import math


def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        result = [0] * (math.ceil(num / 5) + 1)
        for j in range(0, len(result)):
            result[j] = num - j * 5
        result = map(str, result + list(reversed(result))[1:])
        print(" ".join(result) + " ")


if __name__ == '__main__':
    main()
