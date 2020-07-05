import sys

tests = int(input())

l = []
for i in range(tests):
    n = int(input())
    xlist = input().split()
    array = [int(xlist[i]) for i in range(n)]
    array.append(sys.maxsize)
    for j in range(len(array)-1):
        if array[j] > array[j+1]:
            l.append(array[j+1])
        else:
            l.append(-1)
    print(*l)
    l.clear()
