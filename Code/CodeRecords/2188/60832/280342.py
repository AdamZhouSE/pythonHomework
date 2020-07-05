temp = input().split()
n = int(temp[0])
k = int(temp[1])

A = input()
B = input()

q = int(input())

for qq in range(q):
    profit = 0
    ar = list(map(int, input().split()))
    s = ar[0]
    t = ar[1]
    l = ar[2]
    r = ar[3]

    T = A[s - 1:t]
    P = B[l - 1:r]

    i = T.find(P)

    if i == -1:
        profit = 0
    else:
        profit += k - (i + s)
        # T=T[r-l+1+i:]
        i = T.find(P, r - l + 1 + i)
        while i != -1:
            profit += k - (i + s)
            # T=T[r-l+1+i:]
            i = T.find(P, r - l + 1 + i)
    print(profit)
