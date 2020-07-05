t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    days=[]
    i=1
    count=0
    temp=0
    while i<n:
        if arr[i]>arr[i-1]:
            count+=1
        else:
            if count!=0:
                days.append([temp,i-1])
                count=0
            temp=i
        i+=1
        if (i==n-1)&(count!=0):
            days.append([temp,i])
    for i in range(len(days)):
        if i!=len(days)-1:
            print('(%d %d)' %(days[i][0],days[i][1]),end=' ')
        else:
            print('(%d %d)' % (days[i][0], days[i][1]))
