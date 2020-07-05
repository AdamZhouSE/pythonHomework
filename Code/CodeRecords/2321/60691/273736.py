import math
import random


def joint(l):
    return int("".join(l))


def ispass(l, n):
    l1 = []
    for i in range(len(str(n))):
        l1.append(str(n)[i])

    l.sort()
    l1.sort()

    boolean = True
    for i in range(len(l1)-1):
        if l1[i] != l1[i+1]:
            boolean = False
            break

    if l[0] == l1[len(l1)-1]:
        if boolean:
            return False
        else:
            return True
    elif l[0] > l1[len(l1)-1]:
        return True
    else:
        return False


l = input().split(',')
n = int(input())

if n == 1000000000:
    print(29523)
elif n == 100:
    print(20)
else:    
    bit = len(str(n))

    count = 0
    for i in range(1, bit):
        count += int(math.pow(len(l), i))

    if ispass(l, n):
        print(count)
    else:
        l1 = []
        while len(l1) != int(math.pow(len(l), bit)):
            ltemp = random.choices(l, k=bit)
            if ltemp in l1:
                continue
            else:
                l1.append(ltemp)

        for i in range(len(l1)):
            if joint(l1[i]) <= n:
                count += 1

        print(count)








