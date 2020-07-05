n,m = [int(i) for i in input().split(' ')]
arr = [int(i) for i in input().split(' ')]
x = 0
while(x<m):
    x+=1
    temp = [int(i) for i in input().split(' ')]
    if temp[0] == 1:
        x,y,k = temp[1],temp[2],temp[3]
        for i in range(x-1,y):
            arr[i]+=k
    elif temp[0] == 2:
        x,y = temp[1],temp[2]
        su = 0
        for i in range(x-1,y):
            su += arr[i]
        print('%.4f' % (su/(y-x+1)))
        
    else:
        x,y = temp[1],temp[2]
        su = 0
        for i in range(x-1,y):
            su += arr[i]
        aver = (su/(y-x+1))
        res = 0
        for i in range(x-1,y):
            res += (arr[i]-aver)**2
        print('%.4f' % (res/(y-x+1)))