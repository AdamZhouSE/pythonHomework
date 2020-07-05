inp = input().strip().split(" ")
length = int(inp[0])
k = int(inp[1])
stringA = input()
stringB = input()
t = int(input())
for i in range(t):
    profit = 0
    pl = input().strip().split(" ")
    T = stringA[int(pl[0])-1:int(pl[1])]
    P = stringB[int(pl[2])-1:int(pl[3])]
    j = 0
    while j < len(T):
        if T[j:].find(P) == 0:
            profit += k - int(pl[0]) - j
            j += len(P)
        else:
            j += 1
    print(profit)