def threeEqualParts(A:list):
    sumA = sum(A)
    if sumA == 0:
        return [0, 2]
    if sumA % 3:
        return [-1, -1]
    cal = sumA // 3
    tail0, i = 0, len(A) - 1
    while A[i] == 0:
        i -= 1
        tail0 += 1
    lst = [[], [], []]
    tmp, idx, tail = 0, 0, 0
    for a in A:
        if tmp < cal:
            tmp += a
            lst[idx].append(str(a))
        elif tail < tail0:
            if a == 0:
                lst[idx].append(str(a))
                tail += 1
            else:
                return [-1, -1]
        else:
            tmp, tail = 0, 0
            idx += 1
            tmp += a
            lst[idx].append(str(a))
    if int("".join(lst[0])) == int("".join(lst[1])) == int("".join(lst[2])):
        return [len(lst[0]) - 1, len(lst[0]) + len(lst[1])]
    else:
        return [-1, -1]

print(threeEqualParts(list(map(int,input().split(',')))))