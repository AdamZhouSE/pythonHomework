import itertools
import math


def issquare(n):
    if int(math.sqrt(n)) * int(math.sqrt(n)) == n:
        return True
    else:
        return False


def isvalid(l):
    temp = []
    for i in range(len(l) - 1):
        temp.append(int(l[i]) + int(l[i+1]))

    for i in range(len(temp)):
        if not issquare(temp[i]):
            return False
    return True


l = input().split(',')

s = list(itertools.permutations(l))
l1 = []

for i in range(len(s)):
    if isvalid(s[i]):
        l1.append(s[i])

print(len(l1))



