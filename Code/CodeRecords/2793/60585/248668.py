num=input().strip().split(' ')
num=[int(i) for i in num]
n=num[0]
interval=num[1]
if interval==0:
    print(0)
else:
    time=input().strip().split(' ')
    time=[int(i) for i in time]
    count=1
    for i in range(1,n):
        if time[i]-time[i-1]<=interval:
            count+=1
        else:
            count=1
    print(count)