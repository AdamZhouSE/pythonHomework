T = int(input())
for hhh in range(0, T):
    input()
    aList = [int(i) for i in input().split()]
    bList = [int(i) for i in input().split()]
    a = len(aList)
    b = len(bList)
    i = j = 0

    while i < a and j < b:
        if aList[i] < bList[j]:
            print(aList[i], end=' ')
            i += 1
        else:
            print(bList[j], end=' ')
            j += 1
    while i < a:
        print(aList[i], end=' ')
        i += 1
    while j < b:
        print(bList[j], end=' ')
        j += 1
    print()