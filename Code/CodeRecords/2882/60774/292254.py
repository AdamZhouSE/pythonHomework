n = int(input())
numLst = list(map(int,input().split(' ')))
last = numLst[0]
isPeak = False
downward = False
for i in range(1,n):
    cur = numLst[i]
    if(isPeak):
        if(cur < last):
            downward = True
        elif(cur > last):
            print('NO')
            break
    else:
        if(downward):
            if(cur >= last):
                print('NO')
                break
        else:
            if(cur == last):
                isPeak = True
            elif(cur < last):
                downward =True
    last = cur
else:
    print('YES')
    