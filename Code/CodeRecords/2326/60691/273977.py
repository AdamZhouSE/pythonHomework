import math


def calculate(l):
    count = 0
    for i in range(len(l)):
        count += int(l[i]) * int(math.pow(2, len(l) - 1 -i))
    return count


def isequal(i, j, l):
    l1 = l[0: i+1]
    l2 = l[i+1: j]
    l3 = l[j:]

    if calculate(l1) == calculate(l2) and calculate(l2) == calculate(l3):
        return True
    else:
        return False


l = input().split(',')
l1 = []

for i in range(len(l) - 1):
    for j in range(i+2,len(l)):
        if isequal(i, j, l):
            l1.append([i, j])

if len(l1) == 0:
    l1.append([-1, -1])

for i in l1:
    print(i)







