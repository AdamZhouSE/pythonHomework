import sys

tests = int(input())


for i in range(tests):
    n = int(input())
    xlist = input().split()
    array = [int(xlist[i]) for i in range(n)]
    array.append(sys.maxsize)
    for j in range(len(array)-1):
        if array[j] > array[j+1]:
            print(array[j+1], end=' ')
        else:
            print(-1, end=' ')
    print()
