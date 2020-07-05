t = int(input())
for i in range(0,t):
    n = int(input())
    numLst = list(set(map(int,input().split(' '))))
    numLst.sort()
    last = numLst[0]
    count = 1
    max = 0
    for j in range(1,len(numLst)):
        if(numLst[j] == last + 1):
            count = count + 1
        else:
            if(count > max):
                max = count
            count = 1
        last = numLst[j]
    print(max)