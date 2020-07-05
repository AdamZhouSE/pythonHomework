def trisect(A):
    length = len(A)
    count = 0
    for a in A:
        if a == 1:
            count += 1
    if count % 3 != 0:
        return [-1, -1]
    for i in range(0, length):
        for j in range(i+1, length):
            L1 = A[:i+1]
            L2 = A[i+1:j]
            L3 = A[j:]
            if isSame(L1, L2) and isSame(L2, L3):
                return [i, j]
    return [-1, -1]


def isSame(L1, L2):
    beg1 = len(L1)
    for i in range(len(L1)):
        if L1[i] == 1:
            beg1 = i
            break
    beg2 = len(L2)
    for i in range(len(L2)):
        if L2[i] == 1:
            beg2 = i
            break
    if beg1 == len(L1) and beg2 == len(L2):
        return 1
    elif L1[beg1:] == L2[beg2:]:
        return 1
    else: return 0

A = list(map(int,input().split(',')))
print(trisect(A))