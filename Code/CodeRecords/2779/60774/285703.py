t = int(input())
for i in range(0,t):
    n = int(input())
    numLst = list(map(int,input().split(' ')))
    a = min(numLst)
    b = max(numLst)
    k = 1
    while(b * k % a != 0):
        k = k + 1
    print(b * k)