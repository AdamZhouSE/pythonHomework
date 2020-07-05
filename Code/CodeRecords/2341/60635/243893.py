count = int(input())
for n in range(count):
    info = input().split()
    n1 = int(info[0])
    n2 = int(info[1])
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
    a2.sort()
    i, j = 0, 0
    last = n1 - 1
    while i < n1 and j < n2 and last >= 0:
        if a1[i] > a2[j]:
            a1[last], a2[j] = a2[j], a1[last]
            last -= 1
            j += 1
        else:
            i += 1
        if last < i:
            break
    a1.sort()
    a2.sort()
    print(*a1, end=' ')
    print(*a2,end=' \n')
    