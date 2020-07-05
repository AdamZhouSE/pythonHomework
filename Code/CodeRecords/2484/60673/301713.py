t = int(input())
for i in range(0, t):
    num = input().split(' ')
    m = int(num[0])
    n = int(num[1])
    A = input().split(' ')
    B = input().split(' ')
    res = []
    for i in range(0, len(A)):
        if (A[i] in res):
            continue
        else:
            res.append(A[i])
    for j in range(0, len(B)):
        if (B[j] in res):
            continue
        else:
            res.append(B[j])
    print(len(res))


