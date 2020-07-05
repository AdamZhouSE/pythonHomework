def f(a, b, s, t, l, r, K):
    profit = 0
    T = a[s - 1:t]
    P = b[l - 1:r]
    while True:
        if T.find(P) >= 0:
            profit += K - (T.find(P) + s)
            T = T[0:T.find(P)] + ''.join(['0']*len(P)) + T[T.find(P) + len(P):]
        else:
            break
    return profit


K = int(input().strip().split()[1])
a = input().strip()
b = input().strip()
num = int(input().strip())
for i in range(num):
    s = [int(x) for x in input().strip().split()]
    print(f(a, b, s[0], s[1], s[2], s[3], K))

