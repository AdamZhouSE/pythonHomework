def isReverse(numA):
    numA = str(numA)
    listA = list(str(numA))
    listB = []

    for i in range(len(numA) - 1 , -1 , -1):
        listB.append(listA[i])
    if listA == listB:
        return True
    return False

#
L = int(input())
R = int(input())
count = 0
for i in range(L, R + 1):
    if isReverse(i):
        sqr = int(i ** 0.5)
        if sqr ** 2 == i:
            if isReverse(sqr):
                count += 1
print(count)