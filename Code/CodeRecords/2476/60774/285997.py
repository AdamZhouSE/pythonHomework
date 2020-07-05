t = int(input())
for i in range(0,t):
    n = int(input())
    stringLst = list(map(int,input().split(' ')))
    stringLst.sort()
    cost = 0
    while(len(stringLst) > 1):
        stringLst[1] = stringLst[1] + stringLst[0]
        cost = stringLst[1] + cost
        stringLst.remove(stringLst[0])
        stringLst.sort()
    print(cost)