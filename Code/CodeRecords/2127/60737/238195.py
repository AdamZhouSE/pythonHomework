import math


if __name__ == "__main__":
    base = int(input())
    expo = int(input().replace(',', ''))
    print(int(math.pow(base, expo) % 1337))
