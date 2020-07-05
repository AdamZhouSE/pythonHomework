questNum = int(input())

for quest in range(questNum):
    nmx = input().split(' ')
    n = int(nmx[0])
    m = int(nmx[1])
    x = int(nmx[2])

    A = input().split(' ')
    B = input().split(' ')

    for i in range(n):
        A[i] = int(A[i])

    for j in range(m):
        B[j] = int(B[j])

    hasPrint = False
    for num in A:
        restNum = x - num

        if restNum in B:
            print(num, end=' ')
            print(restNum)
            hasPrint = True
    if not hasPrint:
        print(-1)