t = int(input())
for x in range(t):
    N = int(input())
    AN = [int(i) for i in input().split()]
    AN.sort()
    A = []
    B = []
    for i in AN:
        if i not in A:
            A.append(i)
            B.append(1)
        else:
            B[A.index(i)] += 1
    result = ""
    while len(B) > 0:
        valueofmax = max(B)
        indexofmax = B.index(valueofmax)
        for i in range(valueofmax):
            result += str(A[indexofmax])
            result += " "
        A.pop(indexofmax)
        B.pop(indexofmax)
    print(result)
