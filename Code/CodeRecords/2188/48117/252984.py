nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
A = input()
B = input()
questNum = int(input())
profit = 0
realA = A

for i in range(questNum):
    A = realA
    stlr = input().split(' ')
    s = int(stlr[0])
    t = int(stlr[1])
    l = int(stlr[2])
    r = int(stlr[3])
    T = A[s - 1:t]
    P = B[l - 1:r]
    profit = 0
    while P in T:
        rawProfit = A.find(P)
        index = T.find(P)
        profit += k - rawProfit - 1
        T = list(T)
        for k in range(index, index + len(P)):
            T[k] = '0'
        A = list(A)
        for m in range(rawProfit, rawProfit + len(P)):
            A[m] = '0'
        Astr = ''
        for z in A:
            Astr += z
        A = Astr
        Tstr = ''
        for j in T:
            Tstr += j
        T = Tstr

    print(profit)