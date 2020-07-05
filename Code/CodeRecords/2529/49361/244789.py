import collections


def reorderNum(num):
    counter = collections.Counter(str(num))

    n = len(str(num))
    num = 1
    while len(str(num)) < n: num *= 2
    while len(str(num)) == n:
        if collections.Counter(str(num)) == counter:
            return "true"
        num *= 2
    return "false"


num = int(input())
print(reorderNum(num))