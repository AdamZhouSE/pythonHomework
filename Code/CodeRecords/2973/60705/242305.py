def dictionize(string):
    s = set(string)
    d = {}
    for i in s:
        d[i] = string.count(i)
    return d


def match(str1, str2):
    return dictionize(str1) == dictionize(str2)


def count(short, long):
    number = 0
    length = len(short)
    i = 0
    while i + length <= len(long):
        sub_long = long[i:i+length]
        if match(short, sub_long):
            number += 1
        i += 1
    return number


if __name__ == "__main__":
    long_str = input()
    n = int(input())
    total = 0
    for i in range(0, n):
        short_str = input()
        total += count(short_str, long_str)
    print(total)
