T = int(input())
L = [2, 1]
for i in range(T):
    n = int(input())
    length = len(L)
    for i in range(length, n+1):
        L.append(L[length-1]+L[length-2])
        length += 1
    print(L[n])