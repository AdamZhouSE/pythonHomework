t = int(input())
for i in range(0,t):
    N = int(input())
    numLst = list(map(int,input().split(' ')))
    K = int(input())
    multi = 1
    for j in range(0,len(numLst)):
        multi = multi * numLst[j]
    print(multi % K)