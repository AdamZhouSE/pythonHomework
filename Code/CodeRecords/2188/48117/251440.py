nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
A = input()
B = input()
questNum = int(input())

for i in range(questNum):
    stlr = input().split(' ')
    s = int(stlr[0])
    t = int(stlr[1])
    l = int(stlr[2])
    r = int(stlr[3])
    T = A[s:t + 1]
    P = B[l:r + 1]
    if P in T:
        profit = T.find(P)

    print(k - profit)