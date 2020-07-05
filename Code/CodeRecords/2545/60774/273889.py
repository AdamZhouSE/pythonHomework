t = int(input())
for i in range(0,t):
    high = int(input())
    numLst = list(map(int,input().split(' ')))
    numLst = sorted(numLst)
    low = 0
    if(sum(numLst) != 0):
        while(high > low):
            if(sum(numLst[low:high]) > 0):
                high = high - 1
            elif(sum(numLst[low:high]) < 0):
                low = low + 1
            else:
                print('Yes')
                break
        else:
            print('No')
    else:
        print('Yes')