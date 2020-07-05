nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
A = input()
B = input()
questNum = int(input())
profit = 0

for i in range(questNum):
    stlr = input().split(' ')
    s = int(stlr[0])
    t = int(stlr[1])
    l = int(stlr[2])
    r = int(stlr[3])
    T = A[s:t + 1]
    P = B[l:r + 1]
    profit = 0
    while P in T:
        rawProfit = A.find(P)
        index = T.find(P)
        profit += k - rawProfit
        T.replace(T[index, index + len(P)], '0'*len(P))

    print(profit)