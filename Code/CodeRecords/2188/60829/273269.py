n, K = [int(i) for i in input().split(' ')]
A = input()
B = input()
q = int(input())
for j in range(q):
    s, t, l, r = [int(i) for i in input().split(' ')]
    P = B[l-1:r]
    nb = len(P)
    i = s-1
    res = 0
    while i <= t-nb:
        if A[i:i+nb] == P:
            res += K-i-1
            i += nb
        else:
            i += 1
    print(res)